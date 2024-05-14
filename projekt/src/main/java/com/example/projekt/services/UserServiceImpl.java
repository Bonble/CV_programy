package com.example.projekt.services;

import com.example.projekt.models.*;
import com.example.projekt.repositories.ProduktItemRepository;
import com.example.projekt.repositories.RoleRepository;
import com.example.projekt.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserRepository userRepo;
    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private RoleRepository roleRepository;

    @Autowired
    private ProduktItemRepository produktItemRepository;

    /*@Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        Optional <User> user= Optional.ofNullable(userRepo.findByEmail(username));
        if (user.isEmpty()){
            throw new UsernameNotFoundException("Zły email.");
        }
        return new org.springframework.security.core.userdetails.User(user.get().getEmail(), user.get().getPassword(), mapRolesToAuthorities(user.get().getRoles()));
    }*/
    @Override
    public UserDetails loadUserByUsername(String login) throws UsernameNotFoundException {
        Optional<User> user = userRepo.findByEmail(login);
        if(user.isEmpty()){
            new UsernameNotFoundException("User not exists by Username");
        }
        Set<GrantedAuthority> authorities = user.get().getRoles().stream()
                .map((role) -> new SimpleGrantedAuthority(role.getName()))
                .collect(Collectors.toSet());
        return new org.springframework.security.core.userdetails.User(login,user.get().getPassword(),authorities);
    }

    @Override
    public User getUserByUsername(String login) throws UsernameNotFoundException {
        Optional<User> user = userRepo.findByEmail(login);
        if(user.isEmpty()){
            new UsernameNotFoundException("User not exists by Username");
        }
        return user.get();
    }

    public Optional<User> getUserByUsername2(String login) {
        return userRepo.findByEmail(login);
    }

    @Override
    public User save(UserRegisterDto userRegDto) {
        User user = new User();
        user.setEmail(userRegDto.getEmail());
        user.setAdres(userRegDto.getAdres());
        user.setNazwisko(userRegDto.getNazwisko());
        user.setPassword(passwordEncoder.encode(userRegDto.getPassword()));
        //user.setPassword(userRegDto.getPassword());


        List<Role> roles=new ArrayList<Role>();
        Role role=new Role();
        role.setName("ROLE_KLIENT");
        roles.add(role);
        user.setRoles(roles);


        Set<ProduktItem> newsletter = Collections.emptySet();
        //Set<ProduktItem> newsletter = new HashSet<>();
        /*
        long p = 123456;
        Optional<ProduktItem> produkt = produktItemRepository.findByEan(p);
        p = 123456;
        produkt.get().setEan(p);
        newsletter.add(produkt.get());

        p = 56481;
        produkt = produktItemRepository.findByEan(p);
        produkt.get().setEan(p);
        newsletter.add(produkt.get());
        */
        user.setProduktItems(newsletter);
        return userRepo.save(user);
    }
    @Override
    public User saveNewsletter(User user){
        return userRepo.save(user);
    }

    private Collection< ? extends GrantedAuthority> mapRolesToAuthorities(Collection < Role > roles) {
        return roles.stream().map(role-> new SimpleGrantedAuthority(role.getName())).collect(Collectors.toList());
    }
}