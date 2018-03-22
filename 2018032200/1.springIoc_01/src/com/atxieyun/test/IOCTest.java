package com.atxieyun.test;


import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.atxieyun.bean.Person;

public class IOCTest {
	ApplicationContext ioc = new ClassPathXmlApplicationContext("ioc.xml");
	
	@Test
	public void test04(){
		
	}
	
	@Test
	public void test03(){
		Object bean = ioc.getBean("person04");
		System.out.println(bean);
	}
	@Test
	public void test02(){
		Object bean = ioc.getBean("person03");
		System.out.println(bean);
	}
	@Test
	public void test01(){
		
		Person bean = ioc.getBean(Person.class);
		System.out.println(bean);
	}
	@Test
	public void test() {
		//
		
		Person bean =(Person) ioc.getBean("person02");
		
		System.out.println(bean);
	}

}

