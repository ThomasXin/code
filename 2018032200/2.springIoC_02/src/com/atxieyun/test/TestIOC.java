package com.atxieyun.test;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.atxieyun.bean.Person;
/**
 * 
 * @author xiegongzi
 *
 */
public class TestIOC {
	ApplicationContext ioc = new ClassPathXmlApplicationContext("ioc.xml");
	@Test
	public void test03(){
		Person bean = (Person) ioc.getBean("person03");
		
		System.out.println("本人："+ bean );
		
		System.err.println("朋友" + bean.getFriend());
		
	}
	
	@Test
	public void test01(){
		Person bean = (Person) ioc.getBean("person02");
//		System.out.println(bean.getGender().equals("null"));
		System.out.println(bean.getGender()==null);
	}
	@Test
	public void test() {
		Object bean = ioc.getBean("person01");
		System.out.println(bean);
		
	}

}
