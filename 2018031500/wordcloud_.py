# _*_ coding:utf-8 _*_


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba


# 生成词云


def creat_word_cloud(filename):

    text = open("{}.txt".format(filename)).read()

    # jieba分词
    wordlist = jieba.cut(text, cut_all=True)
    wl = "".join(wordlist)

    # 设置词云

    wc = WordCloud(

        # 设置背景颜色
        background_color='white',
        # 设置最大显示的词云数
        max_words=2000,
        # 这种字体都在电脑字体中，一般路径
        font_path=r'C:\Windows\Fonts\simfang.ttf',
        # height=1200,
        # width=1600,
        # 设置字体最大值
        max_font_size=100,
        # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=30,
    )

    # 生成词云
    myword = wc.generate(wl)

    # 展示词云图

    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    # 把词云保存下来
    wc.to_file('py_book.png')

if __name__ == '__main__':
    creat_word_cloud(r'C:\Users\Administrator\Desktop\pc\2018031200\pdf')
