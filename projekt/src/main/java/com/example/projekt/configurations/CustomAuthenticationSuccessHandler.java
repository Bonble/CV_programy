package com.example.projekt.configurations;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.web.authentication.AuthenticationSuccessHandler;
import org.springframework.security.web.authentication.SimpleUrlAuthenticationSuccessHandler;

import java.io.IOException;
import java.util.Collection;

public class CustomAuthenticationSuccessHandler implements AuthenticationSuccessHandler {
    SimpleUrlAuthenticationSuccessHandler klientSuccessHandler =
            new SimpleUrlAuthenticationSuccessHandler("/index-klient");
    SimpleUrlAuthenticationSuccessHandler pracownikSuccessHandler =
            new SimpleUrlAuthenticationSuccessHandler("/index-pracownik");

    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response,
                                        Authentication authentication) throws IOException, ServletException {
        Collection<? extends GrantedAuthority> authorities = authentication.getAuthorities();
        for (final GrantedAuthority grantedAuthority : authorities) {
            String authorityName = grantedAuthority.getAuthority();
            if (authorityName.equals("ROLE_PRACOWNIK")) {
                // if the user is an ADMIN delegate to the adminSuccessHandler
                this.pracownikSuccessHandler.onAuthenticationSuccess(request, response, authentication);
                return;
            }
        }
        // if the user is not an admin delegate to the userSuccessHandler
        this.klientSuccessHandler.onAuthenticationSuccess(request, response, authentication);
    }
}