package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;


@SpringBootApplication
@RestController
@ComponentScan
public class HajibootApplication {

  @GetMapping("/")
  String home() {
    return "Hello world! こんにちは";
  }

  public static void main(String[] args) {
    SpringApplication.run(HajibootApplication.class, args);
  }
}
