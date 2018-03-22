package com.atxieyun.bean;

public class Person {
	 private Integer id;
	 private String name;
	 private String gender;
	 private double salary;
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
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	public double getSalary() {
		return salary;
	}
	public void setSalary(double salary) {
		this.salary = salary;
	}
	@Override
	public String toString() {
		return "Person [id=" + id + ", name=" + name + ", gender=" + gender
				+ ", salary=" + salary + "]";
	}
	public Person(Integer id, String name, String gender, double salary) {
		super();
		this.id = id;
		this.name = name;
		this.gender = gender;
		this.salary = salary;
		System.out.println("有参构造器。。。。");
	}
	public Person() {
		super();
		System.out.println("无参构造器。。。。");
	}
	public Person(Integer id, String name, String gender) {
		super();
		this.id = id;
		this.name = name;
		this.gender = gender;
		System.out.println("gender");
	}
	public Person(Integer id, String name, double salary) {
		super();
		this.id = id;
		this.name = name;
		this.salary = salary;
		System.out.println("salary");
	}
	 
	 
	 
}
