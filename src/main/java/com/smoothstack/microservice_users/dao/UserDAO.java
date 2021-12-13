package com.smoothstack.microservice_users.dao;

import com.smoothstack.microservice_users.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserDAO extends JpaRepository<User, Integer> {

}
