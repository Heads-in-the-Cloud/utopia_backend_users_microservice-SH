package com.smoothstack.microservice_users.service;

import com.smoothstack.microservice_users.dao.UserRoleDAO;
import com.smoothstack.microservice_users.model.UserRole;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserRoleService {

    @Autowired
    private UserRoleDAO userRoleDao;

    public UserRole getById(int role_id) {
        try {
            return userRoleDao.findById(role_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new UserRole();
    }

    public UserRole getByName(String role_name) {
        try {
            return userRoleDao.getByRoleName(role_name);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public List<UserRole> getAllUserRoles() {
        return userRoleDao.findAll();
    }

    public boolean insert(UserRole user_role) {
        try {
            userRoleDao.save(user_role);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean delete(UserRole user_role) {
        try {
            userRoleDao.delete(user_role);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean delete(int role_id) {
        try {
            userRoleDao.deleteById(role_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteUserRoleByName(String role_name) {
        try {
            userRoleDao.deleteUserRoleByName(role_name);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
