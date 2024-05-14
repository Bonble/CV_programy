package com.example.projekt.services;

import com.example.projekt.models.Role;
import com.example.projekt.repositories.RoleRepository;

import java.util.Optional;

public class RoleService{
    RoleRepository roleRepository;
    public Optional<Role> getByName(String name) {
        return roleRepository.findByName(name);
    }
}
