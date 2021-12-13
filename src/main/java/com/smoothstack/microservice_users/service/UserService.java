package com.smoothstack.microservice_users.service;

import com.smoothstack.microservice_users.dao.UserDAO;
import com.smoothstack.microservice_users.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {

    @Autowired
    private UserDAO userDao;


    public User getById(int user_id) {
        try {
            return userDao.findById(user_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new User();
    }

    public List<User> getAllUsers() {
        return userDao.findAll();
    }

    public boolean insertUser(User user) {
        try {
            userDao.save(user);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteUser(User user) {
        try {
            userDao.delete(user);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteUser(int user_id) {
        try {
            userDao.deleteById(user_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
