package test;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * ������֤
 * @author Administrator
 *
 */
public class EmailVerification {
	
	public static void main(String[] args) {
		//������ʽ
		Pattern pattern = Pattern.compile("^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\\.([a-zA-Z0-9_-])+)+$");
		//������������ַ����
		Matcher matcher = pattern.matcher("xhlllcl1314@1.com");
		//�ж��Ƿ���ϣ�������Ϸ���true����������Ϸ���flase
		boolean matches = matcher.matches();
		System.out.println(matches);
	}

}
