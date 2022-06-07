# 全球视野下的犹太文明

CAT PKU

### 《Save the Jews!》 创意作业脚本

#### 制作过程

本创意作业使用Python+PhotoShop+Pixilart制作，整体历时**两周**制作完成。

本游戏使用python语言编写，主要基于pygame库，包含**16*7个python文件，代码量大约有**1400**行。

游戏中使用的图片素材约有136张，其中手工绘制的约有**60**张，使用Pixilart和PS软件绘制。

游戏中使用的背景音乐和代码框架来自教程https://youtu.be/QU1pPzEGrqw

游戏中灵感来源于真实的纳粹屠杀犹太人的事件，所有的参考图片来自谷歌图片。

游戏中的一些改进的建议来自课程老师与助教，谢谢！

#### 安装说明

1. 配置python环境
2. 安装pygame库 （以上两步可以参考教程[Python> pygame安装与配置](https://www.cnblogs.com/fortunely/p/11066814.html)）
3. 下载本游戏代码，链接：
4. 运行代码中的<code>main.py</code>即可

#### 游戏内容

##### 故事背景：

《出埃及记》故事中有摩西带领犹太人逃离埃及，尤其（老师在课堂上展示的视频中）摩西左手升起一道火焰墙阻挡埃及军队，右手一个造出海底通道帮助犹太人离开的样子令人十分震撼。但是为什么二战期间犹太民族受到残忍的迫害时，没有这样的人物帮助他们逃离苦海呢？不！我不接受！起码在我创造的世界里！

主人公安东尼是一个虔诚的犹太男孩，正当他将要跟随家人被塞到火车上运往集中营时，上帝给予了他超凡的力量，他将要利用这股力量打倒纳粹士兵，拯救自己的民族。

##### 故事场景（三个）：

1. 犹太民族将要被赶上前往集中营的火车
2. 奥斯辛威集中营的部分场景
3. 决战希特勒

**游戏界面**

1. 开始界面，有开始游戏，选项，退出三个选择

   1. ![image-20220607224810104](C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607224810104.png)

2. 选项界面，显示了游戏的slogan，“be the Moses of our time!" （启发自与杨梦老师的交流），以及作者的署名

   1. ![image-20220607224836947](C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607224836947.png)

3. 游戏进行界面，有着切换武器，切换魔法，查看图鉴，退出游戏等功能

   1. 武器栏与魔法栏，以及状态栏，功能栏（**因为主人公此前已经遭遇过纳粹的非人对待，所以初始状态血量并不健康）**
      <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607224855472.png" alt="image-20220607224855472" style="zoom:33%;" /><img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607224936682.png" alt="image-20220607224936682" style="zoom:50%;" />

   2. 图鉴提供了游戏中各种元素的细节大图，可以随意切换查看，或者自动放映

      <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607225230498.png" alt="image-20220607225230498" style="zoom:33%;" />
      <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607225055624.png" alt="image-20220607225055624" style="zoom: 10%;" /><img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607225121331.png" alt="image-20220607225121331" style="zoom: 10%;" />

**全局设定**

1. 每一关的关卡都有一段开头文字，使用了托拉图片作为背景，其中的关卡介绍性文字为**希伯来语**，但是为了方便展示，作者（就是我）贴心地提供了中文翻译
   <img src="../Python/MyGame/托拉1.png" alt="托拉1" style="zoom:50%;" />
2. 主人公
   1. 服饰上有四处特别设计了犹太元素，从上往下分别是：头戴的蓝色犹太小帽，系在前额和左臂的经文匣，发型鬓角，披着的祷告巾
      <img src="../Python/MyGame/graphics/player/down/pixil-frame-0.png" alt="pixil-frame-0" style="zoom:150%;" /><img src="../Python/MyGame/graphics/player/left_idle/pixil-frame-0.png" alt="pixil-frame-0" style="zoom:150%;" /> <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220531120123621.png" alt="image-20220531120123621" style="zoom:25%;" />
   2. 武器设计参考了Menorah犹太教烛台，托拉铜手笔yad
      <img src="../Python/MyGame/graphics/weapons/menorah/full.png" alt="full" style="zoom:200%;" /><img src="../Python/MyGame/graphics/weapons/finger/full.png" alt="full" style="zoom:250%;" /><img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220531113801494.png" alt="image-20220531113801494" style="zoom: 15%;" /> <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220531115734529.png" alt="image-20220531115734529" style="zoom:25%;" />
   3. 魔法的设计参考了《出埃及记》当中，摩西阻挡埃及士兵时使用的“火焰墙”魔法，以及原创的治疗魔法，消耗魔力值回复血量
      <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220531183128340.png" alt="image-20220531183128340" style="zoom:33%;" /><img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220531183151409.png" alt="image-20220531183151409" style="zoom:33%;" />

###### level1：阻止！地狱的火车！

**灵感来源**

<img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220530200001941.png" alt="image-20220530200001941" style="zoom: 33%;" />

**关卡文字**

你是一个犹太男孩，你和你的家人还有其他生活在德国的犹太人正在被赶上一辆火车，没错，就是前往“地狱”集中营的火车，不透气的黑暗集装箱，没有一扇窗子，你已经可以预想到自己将要迎接的命运，但你觉得很无奈，你觉得你和其他所有犹太人都不应该止步于此，你们本可以自由地经商，自由地结婚生子，为什么摩西这次没有出现，为什么没有人带领你们逃离，难道上帝抛弃你们了吗......

此时，全身上下突然涌起了无穷的力量，你意识到，上帝从来没有抛弃你们，你就是这个时代的摩西。请解救你的族群吧！

【上下左右】移动，【空格】攻击，【Q】切换武器，【E】切换魔法（在上帝赐予的力量中，你领悟了**火焰魔法**和**治愈魔法**，【Ctrl】使用魔法（消耗MP，但是会自动恢复，请注意使用）

**关卡细节**

1. 平民
   1. 服饰添加了部分犹太特色，如犹太小帽、大卫之星、大黑帽子、头巾
      ![10](../Python/MyGame/graphics/civilians/citizens/10.png) ![16](../Python/MyGame/graphics/civilians/citizens/16.png) ![14](../Python/MyGame/graphics/civilians/citizens/14.png)
   2. 加入了一些眼泪，体现德军的压迫（或许需要放大才能看清）
2. 敌人
   1. 没有攻击目标时会挑动帽子，非常的轻蔑。攻击方式为拿枪顶推，灵感来源于《钢琴师》中的德军，总是喜欢推搡人。
      <img src="../Python/MyGame/graphics/monsters/bamboo/move/moving-0.png" alt="moving-0"  /> <img src="../Python/MyGame/graphics/monsters/bamboo/idle/normal-soldier-1.png" alt="normal-soldier-1"  />
3. 场景
   1. 
   2. 仿照了真实图片中的集中营车厢绘制的车厢
      ![1](../Python/MyGame/graphics/objects/1.png) <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220530195833829.png" alt="image-20220530195833829" style="zoom: 25%;" />

###### level2：击败！地狱的魔鬼！

**关卡文字**

恭喜你打败了上一关的敌人！现在你已经穿越了奥斯威辛集中营那臭名昭著的标语牌“**劳动使人自由**”，来到了“地狱”的中心。看看那些可怜的犹太百姓，可恶的德国士兵殴打、虐待他们，很多人甚至活活饿死。在这块看起来平平无奇的土地上，将来有可能会飘荡百万的亡灵，请你阻止这一切发生！

**关卡细节**

1. 囚犯
   1. 被电网困住，骨瘦如柴，双目含泪
      ![pixil-frame-2](../Python/MyGame/graphics/civilians/prisoners/pixil-frame-2.png) ![pixil-frame-3](../Python/MyGame/graphics/civilians/prisoners/pixil-frame-3.png) <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220530200249577.png" alt="image-20220530200249577" style="zoom:25%;" />
2. 敌人
   1. 士兵：穿着整洁暖和的**纳粹标志大衣**，舒服地抽着香烟，喜欢用囚犯的脸熄灭烟头
      <img src="../Python/MyGame/graphics/monsters/spirit/move/pixil-frame-1 (1).png" alt="pixil-frame-1 (1)" style="zoom:150%;" /> <img src="../Python/MyGame/graphics/monsters/spirit/attack/pixil-frame-7.png" alt="pixil-frame-7" style="zoom:150%;" />
   2. 小boss：穿着帅气逼人，佩戴纳粹标志臂章，喜欢用那锃亮的皮鞋踹人
      <img src="../Python/MyGame/graphics/monsters/squid/attack/pixil-frame-0 (7).png" alt="pixil-frame-0 (7)" style="zoom:150%;" /> <img src="../Python/MyGame/graphics/monsters/squid/attack/pixil-frame-4 (2).png" alt="pixil-frame-4 (2)" style="zoom:150%;" />
3. 场景
   1. 奥斯维辛集中营标语牌，“**劳动使人自由**”
      <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220531181922321.png" alt="image-20220531181922321" style="zoom:50%;" />         <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220530200130435.png" alt="image-20220530200130435" style="zoom:33%;" />
   2. 电网（红色部分是鲜血），可以被攻击拆除
      ![0](../Python/MyGame/graphics/gate/0.png)![1](../Python/MyGame/graphics/gate/1.png)![2](../Python/MyGame/graphics/gate/2.png) <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220530202256549.png" alt="image-20220530202256549" style="zoom:25%;" />
   3. 荒芜的土地上散布的骸骨，是已经逝去的犹太人唯一留下的”遗物“
      <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220531181942274.png" alt="image-20220531181942274" style="zoom:33%;" />

###### level3：决战！最终的敌人！

**关卡文字**

辛苦了！勇士！你成功击败了奥斯维辛集中营的魔鬼们，解放了被困住的犹太人。但是，只要有一个人还存在，那这场屠杀就不可能结束。没错，请你打倒纳粹元首——希特勒！！加油！

**关卡细节**

1. 敌人
   1. 最终BOSS希特勒，穿着花哨（出于个人原创设计，无参考资料），喜欢行纳粹礼，被打败了就会吃氰化物毒药自杀。
      ![pixil-frame-1](../Python/MyGame/graphics/monsters/raccoon/attack/pixil-frame-1.png) ![pixil-frame-3](../Python/MyGame/graphics/monsters/raccoon/attack/pixil-frame-3.png)  ![pixil-frame-4](../Python/MyGame/graphics/particles/raccoon/pixil-frame-4.png)
      
   2. 场景
      1. 模仿了希特勒的书房设计
         ![image-20220607232652689](C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607232652689.png)
      
         ![image-20220531180921228](C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220531180921228.png) <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220530212512350.png" alt="image-20220530212512350" style="zoom: 33%;" />
      
      2. 【战胜希特勒以前】墙壁上的艺术作品来自希特勒的个人画作，地上的雕塑分别与希特勒相关（个人认为）
      
         1. Napoleon Bonaparte Statue Sculpture
      
            > 拿破仑和希特勒两人有时会被拿来做比较，虽然两者有着极大的不同（希特勒的动机源于一种非常可怕的信念，而拿破仑只是一个野心勃勃的机会主义者，他本人对恐怖屠杀之类的根本没有兴趣，他也从来没建立过类似纳粹集中营之类的组织），也正因此可以形成强烈的对比，希特勒或许本来也能成为一个德国的英雄
      
             ![napoleon](../Python/MyGame/napoleon.png)<img src="../Python/MyGame/napoleon.jpg" alt="napoleon" style="zoom:33%;" />
      
         2. 尼采
      
            > 尼采的格言常常被希特勒挂在嘴边，“强人的格言，别理会！让他们去唏嘘！夺取吧！我请你只管夺取！”希特勒也被认为是尼采思想的坚定实践者，将尼采思想付诸行动。
      
            ![nicai](../Python/MyGame/nicai.png)<img src="../Python/MyGame/nietzsche.jpg" alt="nietzsche" style="zoom: 25%;" />
      
         3. 歌德
      
            > 最伟大的德国作家之一，可以作为德国的代表之一，故选取其雕塑放置在希特勒房间。
      
            ![gede](../Python/MyGame/gede.png)<img src="../Python/MyGame/Goethe_Schiller_Weimar_3.jpg" alt="Goethe_Schiller_Weimar_3" style="zoom:25%;" />
      
         4. 希特勒的绘画作品
      
            > 在小的时候，希特勒在玩伴和同学的心中就是一个喜欢画画的孩子，可是希特勒的父亲却不希望自己的儿子希特勒搞什么艺术，父亲希望他能选择吃技术饭，就这样本来在父亲的逼迫下，希特勒只能选择了技术类专业。可是在父亲去世之后，希特勒似乎又看到了自己人生的希望，他决定重新拾起自己的画笔，开始从事绘画工作，就这样希特勒报考了维也纳艺术学院，可是老天却狠狠的捉弄了希特勒一把，两次考试都没有能成功，确实给了希特勒很大的打击。以至于之后的希特勒一度流落街头，混的非常的惨，无奈只能是靠卖画为生。直到一战的爆发，希特勒决定参军入伍，这个举动无疑是奠定了希特勒人生最为关键的一步。
            >
            > 如果，希特勒坚持做了画家，现在的世界又会如何呢？希特勒的魔鬼形象是必然还是偶然？
      
            1. *Nelkenstrauss* (1910)
               <img src="../Python/MyGame/hitpic0.png" alt="hitpic0" style="zoom:33%;" />
            2. *Vienna State Opera House*, Adolf Hitler, 1912![hitpic2](../Python/MyGame/hitpic2.jpg)
            3. 希特勒自画像，传闻是他最早的自画像，当时只有21岁，正在为成为一名艺术家而奋斗，完全不知道自己将来会成为世界的魔头。![hitpic3](../Python/MyGame/hitpic3.jpg)
      
      3. 【战胜希特勒之后】，墙壁上的艺术绘画和地上的雕塑会焚烧起来，换成犹太艺术家的画作以及与犹太有关的雕塑作品
         ![3](../Python/MyGame/graphics/particles/pic1/3.png)![pixil-frame-0](../Python/MyGame/graphics/particles/statue4/pixil-frame-0.png)
      
         1. **马克·夏卡尔**
            
            > (白俄罗斯犹太裔的俄法著名艺术家)
            
            <img src="E:\Document\Codes\Python\MyGame\painting1.png" alt="painting1" style="zoom:30%;" /> <img src="E:\Document\Codes\Python\MyGame\painting2.png" alt="painting2" style="zoom: 25%;" />
            左：To Russia, to the Asses and Others，1911
            右：The Praying Jew, 1923
            比起这位作家其他更出名的作品，我特意选择这两幅作品添加到我的作品之中。
            
            > 首先第一幅作品描绘了一个非常奇妙而又自然的，仿佛出现在梦境一般的场景，一个挤奶女工，却像众神的使者一样飘在如宇宙般的黑暗地带中，下方一头红牛静静地站在村庄地屋顶上喂食着小牛和孩子。温暖的乡村景象和神秘的宇宙地带形成了强烈的对比，究竟什么是真实，什么又是虚幻？**二战期间犹太人所经历痛苦和世界上其他地区幸福生活着的人们似乎也形成了一种荒诞的，令人眼花缭乱的对比**。
            > 再看第二幅作品，描绘了一位身着了完整的祈祷服饰的犹太人，首先其中出现的犹太小帽、前额与左臂缠绕的经文匣、身披的祷告巾，都**与我主人公的设定一致**，是一个小的彩蛋。其次，据我了解，画家在1923年画这副作品时，是希望能保持与过去那个犹太世界的联系，尽管过去对他来说已经非常困难（他曾被拘留近十年），但他在做这幅画时，显然想象不到，在二十年后的世界，犹太人会面临更大的威胁，**这是一个历史跨度上的前后呼应，也是一个小小的彩蛋**。
            
         2. **伊西多尔·考夫曼**
            
            > （奥匈帝国画家，出生于匈牙利王国阿拉德。其父母是匈牙利犹太人。考夫曼的绘画作品大多与犹太人有关)
            
            <img src="E:\Document\Codes\Python\MyGame\painting3.png" alt="painting3" style="zoom:30%;" />
            Friday Evening， 1920
      
            （***Friday Evening*** depicts a traditionally attired woman seated beside a table prepared for the inauguration of the Sabbath. ）
            
            > 我选择这幅画是因为这正描绘了安息日的夜晚，也是我们课程中老师提到的词汇，如果可以以游戏中的彩蛋形式出现的话，可以再次加深同学的印象。
            
         3. 雕塑作品
      
            1. Samuel Halevi Abulafia’s bust in Toledo, Spain
               （撒母耳，拯救以色列脱离士师时代的危难绝望，转入君主政制的平安兴盛时代的民族英雄）
      
               <img src="E:\Document\Codes\Python\MyGame\standing3.png" alt="standing3" style="zoom: 200%;" /><img src="C:\Users\Anton\AppData\Roaming\Typora\typora-user-images\image-20220531154110563.png" alt="image-20220531154110563" style="zoom:33%;" />
      
            2. The Jewish Woman of Algiers， 1862
               
               （Algiers，阿尔吉亚，位于非洲，19世纪时就有少部分的犹太人生活在那里，便有这么一座描绘了非洲犹太女性形象的雕塑。）
               
               > 我选择这座雕像是因为，我本人在此之前也有个刻板印象以为犹太人就只有白人，但是通过课程的学习以及这个创意作业的制作过程中了解到原来非洲也有犹太人，于是便想把这个发现以游戏元素的形式永久记录下来。
      
               <img src="E:\Document\Codes\Python\MyGame\standing2.png" alt="standing2" style="zoom: 150%;" /><img src="E:\Document\Codes\Python\MyGame\standing2.JPG" alt="standing2" style="zoom: 7%;" />
               
            3. Licoricia of Winchester Appeal
               （利科里亚，一位英籍犹太女性，也是13世纪中世纪英国最富有和最杰出的犹太女性。她涉及的主要生意是放贷，她的顾客甚至包括了当时的英格兰国王亨利三世，足以说明她的影响力之大。当她不幸在街上遇刺时，她的死讯甚至传到了德国的犹太社区当中，引起了世界上许多人的关注。）
      
               > 在众多备选里面，选择这座犹太形象雕像，一是因为它刻画的主角比较出名，有比较深的影响力。二是出于个人想法。我们知道圣经时代奠定了犹太社会传统的“男主内，女主外”的思想，女性没有权利和男子一样接受教育、参加公共宗教生活，婚姻问题上也处于被动地位，《圣经》中丈夫可以随心所欲休妻构成了中世纪以前整个犹太离婚法的实质内核。但是中世纪时期，尽管犹太妇女依然处于边缘化的附属地位，但与之前相比已经有了非常积极的变化，其中便包括了可以参加经济生活这一点，正如利科里亚那样在借贷业方面表现出色。这样的变化在等级森严的男权社会中非常难得，也让我印象深刻，因此个人想要在自己的游戏中纪念这一个人物。（顺便招招财）
               
               <img src="E:\Document\Codes\Python\MyGame\standing1.png" alt="standing1" style="zoom: 150%;" /><img src="E:\Document\Codes\Python\MyGame\standing1.JPG" alt="standing1" style="zoom: 67%;" />
      
         4. 击败希特勒后，会出现一道传送门，意味着主人公将要去解救更多地方的犹太人民
            <img src="C:/Users/Anton/AppData/Roaming/Typora/typora-user-images/image-20220607232957820.png" alt="image-20220607232957820" style="zoom:33%;" />
            
         4. 在传送门上停留一段时间后，游戏通关，通关界面采用了一张犹太孩童们开心大笑的照片，表现了在主人公打倒希特勒后，犹太民族过上的幸福自由的生活
      
            <img src="../Python/MyGame/ending.png" alt="ending" style="zoom:50%;" />

