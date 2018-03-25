package test;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * 邮箱验证
 * @author Administrator
 *
 */
public class EmailVerification {
	
	public static void main(String[] args) {
		//正则表达式
		Pattern pattern = Pattern.compile("^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\\.([a-zA-Z0-9_-])+)+$");
		//将输入的邮箱地址进行
		Matcher matcher = pattern.matcher("xhlllcl1314@1.com");
		//判断是否符合，如果符合返回true，如果不符合返回flase
		boolean matches = matcher.matches();
		System.out.println(matches);
	}

}
