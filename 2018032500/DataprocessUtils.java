package test;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class DataprocessUtils {
	/**
	 * MD5����
	 * @param source ����
	 * @return ����
	 */
	public static String md5(String source){
		//�����ж��Ƿ�Ϊnull���߳���Ϊ��
		if (source==null || source.length()==0) {
			return source;
		}
		
		//1.׼������
		char [] c = new char[]{'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
		StringBuilder builder = new StringBuilder();
		
		//2.��ȡMessageDigest����
		MessageDigest digest = null;
		try {
			digest = MessageDigest.getInstance("md5");
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
		
		//3.��ȡԴ�ַ������ֽ�����
		byte[] bytes = source.getBytes();
		
		//4.ִ�м��ܲ���
		byte[] target = digest.digest(bytes);
		
		//5.�����ֽ�����
		for (int i = 0; i < target.length; i++) {
			
			byte b = target[i];
			
			//6.ȡ����λ�͵���λ��ֵ
			int high = (b >> 4) & 15;
			int low = b & 15;
			
			//7.��ȡ��Ӧ���ַ�
			char highChar = c[high];
			char lowChar = c[low];
			
			//8.ƴװ�ַ���
			builder.append(highChar).append(lowChar);
			
		}
		
		return builder.toString();
		
	}
}