package test;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class DataprocessUtils {
	/**
	 * MD5加密
	 * @param source 明文
	 * @return 密文
	 */
	public static String md5(String source){
		//首先判断是否为null或者长度为零
		if (source==null || source.length()==0) {
			return source;
		}
		
		//1.准备工作
		char [] c = new char[]{'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
		StringBuilder builder = new StringBuilder();
		
		//2.获取MessageDigest对象
		MessageDigest digest = null;
		try {
			digest = MessageDigest.getInstance("md5");
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
		
		//3.获取源字符串的字节数组
		byte[] bytes = source.getBytes();
		
		//4.执行加密操作
		byte[] target = digest.digest(bytes);
		
		//5.遍历字节数组
		for (int i = 0; i < target.length; i++) {
			
			byte b = target[i];
			
			//6.取高四位和低四位的值
			int high = (b >> 4) & 15;
			int low = b & 15;
			
			//7.获取对应的字符
			char highChar = c[high];
			char lowChar = c[low];
			
			//8.拼装字符串
			builder.append(highChar).append(lowChar);
			
		}
		
		return builder.toString();
		
	}
}