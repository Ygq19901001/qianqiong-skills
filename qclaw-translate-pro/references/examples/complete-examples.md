<!-- SECLEVEL: INTERNAL -->

# 完整示例

## 📋 完整示例

### 示例1：商务邮件翻译（英译中）

**用户请求**：「翻译这段商务邮件：Dear Mr. Chen, I hope this email finds you well. I'm writing to follow up on our conversation last Tuesday regarding the Q3 supply agreement. We've reviewed the revised terms and are generally satisfied with the pricing structure. However, we would appreciate some clarification on the delivery timeline — specifically whether the July batch can be expedited by two weeks. Please let us know your thoughts at your earliest convenience. Best regards, James Wilson, Procurement Director, GlobalTech Inc.」

---

【译文】

陈先生，您好。

上周二我们谈到第三季度供货协议的事，我来跟进一下。

修改后的条款我们看过了，价格结构基本没问题。不过有一点需要您这边帮忙确认——交货时间这块，7月那批货能不能提前两周？方便的时候回复我即可。

祝好

James Wilson
GlobalTech 采购总监

---

【翻译说明】
- **场景**：S2（商务邮件翻译）
- **主要策略**：意译为主——中文商务邮件讲究简洁体面，英文客套需要归化
- **L层级**：达到 L3（场景地道）
- **关键决策**：
  1. "I hope this email finds you well" → 删除。中文商务邮件不需要这个开头，过于西式客气
  2. "at your earliest convenience" → "方便的时候"而非"尽早回复"。原文是礼貌催促不是命令，中文太直白会显得在催
  3. "we would appreciate some clarification" → "需要您帮忙确认"。英文的委婉请求在中文中直接说更自然
  4. "Best regards" → "祝好"。中文商务邮件结尾惯例
- **称呼转换**：Dear Mr. Chen → 陈先生，您好

【质量自评】
准确度9 | 通顺度9 | 地道度9 | 风格度8 | 实用度9 | 诚实度10 → 总分54/60

---

### 示例2：技术文档翻译（英译中）

**用户请求**：「翻译这段技术说明：To configure the API endpoint, set the environment variable API_BASE_URL to your server address. Note that this value must include the protocol prefix (https://) and should not contain a trailing slash. The authentication token is passed via the Authorization header using the Bearer scheme.」

---

【译文】

配置 API 端点时，将环境变量 `API_BASE_URL` 设为你服务器的地址。注意该值必须包含协议前缀（`https://`），且末尾不能带斜杠。身份验证令牌通过 `Authorization` 头部以 Bearer 方式传递。

---

【翻译说明】
- **场景**：S4（技术文档翻译）
- **主要策略**：直译——技术文档准确第一
- **L层级**：达到 L3（场景地道）
- **关键决策**：
  1. `API_BASE_URL`、`Authorization`、`Bearer` → 保留原文不翻译（技术文档惯例）
  2. "set the environment variable … to …" → "将环境变量 … 设为 …"（中文技术文档惯例表达）
  3. "should not contain" → "不能"而非"不应"（技术文档中should的力度接近于must）
  4. 代码/命令保留原文格式，加反引号标记

【质量自评】
准确度10 | 通顺度9 | 地道度10 | 风格度9 | 实用度10 | 诚实度10 → 总分58/60

---

### 示例3：产品文案本地化（中译英）

**用户请求**：「把这段产品介绍翻成英文，要适合美国市场：本款智能手表，让健康管理触手可及。24小时心率监测，血氧检测，睡眠分析，守护你的每一刻。限时特惠，到手仅需 ¥999。」

---

【译文】

Your health, right on your wrist.

24/7 heart rate monitoring. Blood oxygen tracking. Sleep insights. Everything you need to stay on top of your health — all day, all night.

Limited-time offer: just $139.

---

【翻译说明】
- **场景**：S8（产品文案本地化）
- **主要策略**：本地化——不是翻译，是重新创作
- **L层级**：达到 L4（风格匹配）
- **关键决策**：
  1. "让健康管理触手可及" → "Your health, right on your wrist"——不是字面翻译，是找到了英文广告中功能对等的表达
  2. "守护你的每一刻" → "all day, all night"——避免了直译"safeguard every moment"的过度承诺（美国市场对健康声称更严格）
  3. ¥999 → $139 —— 根据产品品类和价格定位做了市场适配（不是汇率直算），标注了约合汇率换算
  4. "限时特惠，到手仅需" → "Limited-time offer: just" —— 英文电商惯例短句
- **本地化处理**：
  - 保留了产品功能描述（心率/血氧/睡眠），这是通用健康卖点
  - 调整了表达方式以适配美国市场广告法规和消费者偏好
  - 中文的四字节奏感转换成了英文的短句排比感

【备选译法】
- 方案B（更直白风格，适合亚马逊产品描述）：
  > Take control of your health with this smartwatch. Features include 24/7 heart rate monitoring, blood oxygen measurement, and sleep tracking. Now available at a special price of $139.

【质量自评】
准确度8 | 通顺度9 | 地道度9 | 风格度9 | 实用度9 | 诚实度10 → 总分54/60

---

### 示例4：中日商务互译（日译中）

**用户请求**：「翻译这段日文商务邮件：株式会社テクノソリューション 山田様

いつも大変お世話になっております。株式会社フューチャーリンクの佐藤でございます。

先日ご依頼いただきました見積書について、社内で検討を重ねた結果を添付ファイルにてお送りいたします。
今回のご提案では、当初のご予算にできる限り近づけるべく、一部仕様の見直しを行っております。
具体的には、サーバーのスペックを一段階下げることで、初期費用を約15%削減いたしました。
パフォーマンス面での影響は軽微であることを確認しておりますので、ご安心いただければと存じます。

なお、本件につきまして、来週中を目途に一度お打ち合わせの機会をいただけますと幸いです。
ご多忙の折とは存じますが、ご都合の良い日程をいくつかご教示いただけますでしょうか。

何卒よろしくお願い申し上げます。

佐藤健一
株式会社フューチャーリンク
営業部 部長
〒150-0043 東京都渋谷区道玄坂1-2-3
TEL: 03-1234-5678」

---

【译文】

Techno Solution 公司 山田先生/女士：

感谢您一直以来的关照。我是 Future Link 公司的佐藤。

关于前些天您委托我们提供的报价方案，我司内部经反复讨论后已形成最终方案，详见附件。

本次提案为尽可能贴近贵司初始预算，我们对部分规格进行了调整。具体而言，将服务器配置下调一档，使初期费用降低约15%。经确认，调整后的性能影响微乎其微，敬请放心。

此外，关于本项事宜，希望能于下周内安排一次当面沟通。深知您公务繁忙，烦请告知您方便的日期（提供几个备选即可）。

再次感谢。

佐藤健一
Future Link 株式会社 营业部部长
〒150-0043 东京都涩谷区道玄坂1-2-3
电话：03-1234-5678

---

【翻译说明】
- **场景**：S2（商务邮件翻译）
- **语言对**：日→中
- **主要策略**：意译为主——日语商务邮件的敬语体系繁复，需要在中文中找到对等的礼仪感而非逐词对应
- **L层级**：达到 L3（场景地道）
- **关键决策**：
  1. 「いつも大変お世話になっております」→ "感谢您一直以来的关照"——这是日语商务邮件的固定开场白，不是字面意思的"受您照顾"。中文找了对等功能表达，保留了礼貌但避免了日式表达的违和感。
  2. 「株式会社テクノソリューション 山田様」→ "Techno Solution 公司 山田先生/女士"——日本公司名在中文商务邮件中保留原文或音译皆可，此处选择保留。`様`根据性别不明的语境，标注"先生/女士"。
  3. 「社内で検討を重ねた結果」→ "内部经反复讨论后"——日语"検討"不等于中文"检讨"（这是个著名假朋友），而是"讨论/研究"。
  4. 「ご安心いただければと存じます」→ "敬请放心"——日语冗长的敬语表达在中文中需要压缩，保留核心意思和礼貌感即可。
  5. 「何卒よろしくお願い申し上げます」→ "再次感谢"——这是日语邮件最常用的结尾语，字面无法翻译。中文商务邮件结尾需要找到一个功能对等的结束语，此处选择了简洁的"再次感谢"。
  6. 地址信息：日本地址格式保留原文即可，中文读者能理解。电话的国际区号+81未添加（原文无）。
- **敬语处理**：
  - 日语敬语（です・ます体 + 谦让语「いただく」「申し上げる」等）→ 中文通过"敬请""烦请""深感"等礼貌用词传达同等敬意
  - 不自创日语式中文化（如"承蒙关照"过度堆砌）

【日译中常见假朋友提示】
| 日语原文 | 假朋友陷阱 | 正确翻译 |
|----------|-----------|----------|
| 検討する | ≠ 检讨 | 讨论、研究、考虑 |
| 大変 | ≠ 大变 | 非常、很 |
| 結構です | ≠ 结构 | 可以/不用了（根据上下文） |
| よろしくお願いします | 无直接对应 | 根据场景译为"麻烦您了""拜托了""谢谢"等 |
| 迷惑 | ≠ 迷惑 | 麻烦、打扰、困扰 |
| 手紙 | ≠ 手纸 | 信件 |
| 勉強 | ≠ 勉强 | 学习 |
| 丈夫 | ≠ 丈夫 | 结实、坚固 |

【质量自评】
准确度9 | 通顺度9 | 地道度9 | 风格度8 | 实用度9 | 诚实度10 → 总分54/60

---

