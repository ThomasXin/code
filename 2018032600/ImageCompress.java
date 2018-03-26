package test;
import java.awt.image.BufferedImage;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import com.sun.image.codec.jpeg.JPEGImageEncoder;
import com.sun.image.codec.jpeg.JPEGCodec;

import javax.imageio.ImageIO;



/**
 * �������ݵĵ���
 * @author Administrator
 *
 */
@SuppressWarnings("restriction")
public class ImageCompress {
	
	/**
	 * ��ͼƬѹ���������ĳ������ѹ��Ϊ100��ȵ�jpgͼƬ
	 * @param inputStream
	 * @param realPath /surveyLogosĿ¼����ʵ·��������û��б��
	 * @return �����ɵ��ļ�·������ surveyLogos/4198393905112.jpg
	 */
	public static String resizeImages(InputStream inputStream, String realPath) {
		
		OutputStream out = null;
		
		try {
			//1.����ԭʼͼƬ��Ӧ��Image����
			BufferedImage sourceImage = ImageIO.read(inputStream);

			//2.��ȡԭʼͼƬ�Ŀ��ֵ
			int sourceWidth = sourceImage.getWidth();
			int sourceHeight = sourceImage.getHeight();
			
			//3.����Ŀ��ͼƬ�Ŀ��ֵ
			int targetWidth = sourceWidth;
			int targetHeight = sourceHeight;
			
			if(sourceWidth > 100) {
				//������ѹ��Ŀ��ͼƬ�ĳߴ�
				targetWidth = 100;
				targetHeight = sourceHeight/(sourceWidth/100);
				
			}
			
			//4.����ѹ�����Ŀ��ͼƬ��Ӧ��Image����
			BufferedImage targetImage = new BufferedImage(targetWidth, targetHeight, BufferedImage.TYPE_INT_RGB);
			
			//5.����Ŀ��ͼƬ
			targetImage.getGraphics().drawImage(sourceImage, 0, 0, targetWidth, targetHeight, null);
			
			//6.����Ŀ��ͼƬ�ļ���
			String targetFileName = System.nanoTime() + ".jpg";
			
			//7.����Ŀ��ͼƬ��Ӧ�������
			out = new FileOutputStream(realPath+"/"+targetFileName);
			
			//8.��ȡJPEGͼƬ������
			JPEGImageEncoder encoder = JPEGCodec.createJPEGEncoder(out);
			
			//9.JPEG����
			encoder.encode(targetImage);
			
			//10.�����ļ���
			return "surveyLogos/"+targetFileName;
			
		} catch (Exception e) {
			
			e.printStackTrace();
			
			return null;
		} finally {
			//10.�ر���
			if(out != null) {
				try {
					out.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			
		}
	}
}
