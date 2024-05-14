package com.example.projekt.services;

import com.example.projekt.models.User;
import com.example.projekt.models.UserRegisterDto;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;

public interface UserService extends UserDetailsService {
    User getUserByUsername(String login) throws UsernameNotFoundException;

    User save(UserRegisterDto userRegDto);

    User saveNewsletter(User user);
}
