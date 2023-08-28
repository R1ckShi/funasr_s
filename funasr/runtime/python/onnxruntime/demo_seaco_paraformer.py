# coding:utf-8
from funasr_onnx import SeACoParaformer2 as SeACoParaformer
from pathlib import Path

model_dir = "/Users/shixian/code/speech_seaco_paraformer2"
model = SeACoParaformer(model_dir, batch_size=1)
# model = Paraformer(model_dir, batch_size=1, device_id=0)  # gpu

# when using paraformer-large-vad-punc model, you can set plot_timestamp_to="./xx.png" to get figure of alignment besides timestamps
# model = Paraformer(model_dir, batch_size=1, plot_timestamp_to="test.png")

# wav_path = ['{}/.cache/modelscope/hub/damo/speech_paraformer-large-contextual_asr_nat-zh-cn-16k-common-vocab8404/example/asr_example.wav'.format(Path.home())]
wav_path = ['/Users/shixian/Downloads/sac_test.wav']
hotwords = '一流讲师 万达理想汽车 世博 世间 东江 丝印 两岸 中心精神家园 中心线 临江 九寨 九洲 事迹 互质 交通领域 产业园 产区 产品体系 产品店家 京东快递 人类星球 仙剑 仙桃 伊顿 伊顿康明斯 传播保险 传播天使呢 体育课 佛学院 佳人 依赖型 侦查员 侧翻 侧翻事故 保险多元化 保险行业 保险顾问 信号 候鸟 倾侧 停车场 儒教 充值 党费 兜底 全手工 兰溪 农业大学经济技术 冯骥才 冰晶 冷库 刑事强制措施 列阵 利息 制作技艺 券商证券公司指数 加行 勇者 北京 北京南站 北京宫灯 北京节点 匝道 华洋 博雅 卡号 卡塔 卫浴 历史价值 双鸭山 发酵粉 台式电脑 合同效力 唐诗 商场 国庆福利 国教 国策 图标 图案 地缘风险极 坚果 城乡经济 处女座 大肚子 天使 天使投资人 天坛 天气系统 天然气价格 安吉拉芭比 宏观周期共振 官方链接 宫灯 导师 导游团队管理 射击游戏 小牛 市场风险 年份 度数 开源证券 开瓶器 戒色 房屋合同 手提袋 手机业务 技艺 护肤方案 教科文 教科文组织 整体造型 整流罩 文化遗产 文昌 文昌航天 文昌雷达 文昌飞行 斗气 新兵营 新能源保险 新能源汽车 暗黑 月橡木桶 有机菜市场 服务期 木桶 杯子 橡木 正楷 比亚迪 汉堡三角兔 汽车产品专家 汽车轮胎 汽车配件 法国皇帝 法师 活力 海外市场 海鲜产品 游资 湖南长沙国际 烟酒价格 爆率 牛柳 物美 物质文化遗产 物质文化遗产名录 物质文化遗产媒介 特斯拉 特色社会主义思想 王老吉 珍藏 珍藏顶级 理想汽车 理想汽车零售 电源系统设备 电脑小图标 盗墓游戏 真空 眼霜 知识系统 石榴 社会主义 社会主义建设 科学价值 科文 租赁合同 秦皇岛理想汽车 移动互联网 空间造型 等级 管理团队 精度 系列经典版本 纳斯达克市场 经典 缴纳企业年金 美容行业 联合国教科文组织 联盟法师 肚子 股市 股市收盘 股票摘牌 股票账户 芭比 英语 英语试卷 葡萄 葡萄酒 被保险人姓名 西南证券 西沙 西藏 视频发布 视频调解 视频链接 解压视频 证券公司 证券账户 课程研发 资本市场 超能法师 载荷 运动投保人 运载 逆向价值 郁金香造型 酒精 酒精度 酒精检测 铜鼓 长沙 长沙教育 防晒霜 隔离防晒霜 雨燕 雷达 韵母 项目前置 领域 风险承受能力 飞行器 马克思主义 马克思社会主义 驾驶领域 高新技术产业园区 黑龙江省双鸭山市 鼻音 鼻韵母'
# hotwords = '戒色'
result = model(wav_path, hotwords)
print(result)