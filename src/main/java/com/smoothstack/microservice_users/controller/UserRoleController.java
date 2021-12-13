package com.smoothstack.microservice_users.controller;

import com.smoothstack.microservice_users.model.UserRole;
import com.smoothstack.microservice_users.service.UserRoleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/user_role")
public class UserRoleController {

    @Autowired
    private UserRoleService userRoleService;

    @GetMapping(path = "/{role_id}")
    public UserRole getById(@PathVariable int role_id) {
        return userRoleService.getById(role_id);
    }

    @GetMapping(path = "/name={role_name}")
    public UserRole getById(@PathVariable String role_name) {
        return userRoleService.getByName(role_name);
    }

    @GetMapping(path = "/all")
    public List<UserRole> getAllTypes() {
        return userRoleService.getAllUserRoles();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody UserRole user_role) {
        return userRoleService.insert(user_role);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody UserRole user_role) {
        return userRoleService.delete(user_role);
    }

    @PostMapping(path = "/delete/{role_id}")
    public boolean delete(@PathVariable int role_id) {
        return userRoleService.delete(role_id);
    }
}
