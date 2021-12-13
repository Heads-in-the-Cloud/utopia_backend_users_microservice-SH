package com.smoothstack.microservice_users.model;

import javax.persistence.*;

@Entity
@Table(name = "user_role")
@NamedQuery(name = "UserRole.getByRoleName",
            query = "SELECT u FROM UserRole u WHERE u.name LIKE CONCAT('%', ?1, '%')")
@NamedQuery(name = "UserRole.deleteUserRoleByName",
            query = "DELETE FROM UserRole u WHERE u.name LIKE ?1")
public class UserRole {

    @Id
    @Column(name = "id")
    private Integer id;

    @Column(name = "name")
    private String name;



    public UserRole() {};

    public UserRole(Integer id, String name) {
        this.id = id;
        this.name = name;
    }

    public String toString() {
        return String.format("Role %d --> %s", this.id, this.name);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
