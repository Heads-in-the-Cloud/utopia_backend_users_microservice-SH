package com.smoothstack.microservice_users.controller;

import com.smoothstack.microservice_users.model.User;
import com.smoothstack.microservice_users.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/user")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping(path = "/{user_id}")
    public User getById(@PathVariable int user_id) {
        return userService.getById(user_id);
    }

    @GetMapping(path = "/all")
    public List<User> getAllTypes() {
        return userService.getAllUsers();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody User user) {
        return userService.insertUser(user);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody User user) {
        return userService.deleteUser(user);
    }

    @PostMapping(path = "/delete/{user_id}")
    public boolean delete(@PathVariable int user_id) {
        return userService.deleteUser(user_id);
    }
}
