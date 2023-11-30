import 'dart:convert';

import 'package:client/models/user.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<User> users = [];
  final _formKey = GlobalKey<FormState>();
  double currentScoreValue = 0;

  Future<void> _fetchUser() async {
    debugPrint("Fetching User");
    const url = "http://localhost:8000/user/";
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final body = response.body;
    final json = jsonDecode(body);
    if (json["code"] == 200) {
      final result = json["data"] as List<dynamic>;
      final transform = result.map((user) {
        return User(
          email: user['email'],
          fullname: user['fullname'],
          score: user['score'],
          vipLevel: user['vip_level'],
        );
      }).toList();
      setState(() {
        users = transform;
      });
      debugPrint("Fetch completed");
    } else {
      debugPrint("Fetch failed");
    }
  }

  @override
  void initState() {
    super.initState();
    _fetchUser();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text("User List"),
      ),
      body: ListView.builder(
        itemBuilder: (context, index) {
          final user = users[index];
          return ListTile(
            leading: CircleAvatar(child: Text('${index + 1}')),
            title: Text(user.fullname),
            subtitle: Text(user.email),
          );
        },
        itemCount: users.length,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          showDialog(
            context: context,
            builder: (context) {
              return AlertDialog(
                content: Stack(
                  clipBehavior: Clip.none,
                  children: [
                    Positioned(
                      right: -40,
                      top: -40,
                      child: InkResponse(
                        child: const CircleAvatar(
                          backgroundColor: Colors.red,
                          child: Icon(Icons.close),
                        ),
                        onTap: () {
                          Navigator.of(context).pop();
                        },
                      ),
                    ),
                    Form(
                      key: _formKey,
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          TextFormField(),
                          TextFormField(),
                          Slider(
                            value: currentScoreValue,
                            max: 9,
                            divisions: 9,
                            label: currentScoreValue.round().toString(),
                            onChanged: (double value) {
                              setState(() {
                                currentScoreValue = value;
                              });
                            },
                          )
                        ],
                      ),
                    )
                  ],
                ),
              );
            },
          );
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
