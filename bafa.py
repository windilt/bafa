import datetime
import cnlunar

def get_realtime_bafa():
    # 1. 获取当前系统时间
    now = datetime.datetime.now()
    ln = cnlunar.Lunar(now, godType='8char')
    
    # 2. 获取干支信息
    try:
        ri_gan_zhi = ln.day8Char
        shi_gan_zhi = ln.twohour8Char
    except AttributeError:
        ri_gan_zhi = ln.eight_char[2]
        shi_gan_zhi = ln.eight_char[3]

    ri_gan, ri_zhi = ri_gan_zhi[0], ri_gan_zhi[1]
    shi_gan, shi_zhi = shi_gan_zhi[0], shi_gan_zhi[1]

    # 3. 数值映射
    scores = {"甲":9, "己":9, "子":9, "午":9, "乙":8, "庚":8, "丑":8, "未":8,
              "丙":7, "辛":7, "寅":7, "申":7, "丁":6, "壬":6, "卯":6, "酉":6,
              "戊":5, "癸":5, "辰":5, "戌":5, "巳":4, "亥":4}

    # 4. 穴位映射 (卦象, 主穴, 位置提示, 通脉, 配穴, 配穴位置)
    bafa_data = {
        1: ("坎", "申脉", "足外踝正下方凹陷中", "阳跷脉", "后溪", "握拳时，小指掌指关节后肉际处"),
        2: ("坤", "照海", "足内踝尖正下方凹陷处", "阴跷脉", "列缺", "桡骨茎突上方，两手虎口交叉食指尽处"),
        3: ("震", "外关", "腕背横纹上2寸，尺骨与桡骨之间", "阳维脉", "足临泣", "足背外侧，第4/5跖骨底之间凹陷处"),
        4: ("巽", "足临泣", "足背外侧，第4/5跖骨底之间凹陷处", "带脉", "外关", "腕背横纹上2寸，尺骨与桡骨之间"),
        6: ("乾", "公孙", "足内侧缘，第1跖骨基底前下方", "冲脉", "内关", "腕横纹上2寸，两筋(掌长/桡侧腕屈肌)之间"),
        7: ("兑", "后溪", "握拳时，小指掌指关节后肉际处", "督脉", "申脉", "足外踝正下方凹陷中"),
        8: ("艮", "内关", "腕横纹上2寸，两筋(掌长/桡侧腕屈肌)之间", "阴维脉", "公孙", "足内侧缘，第1跖骨基底前下方"),
        9: ("离", "列缺", "桡骨茎突上方，两手虎口交叉食指尽处", "任脉", "照海", "足内踝尖正下方凹陷处")
    }

    # 5. 计算逻辑
    total = scores[ri_gan] + scores[ri_zhi] + scores[shi_gan] + scores[shi_zhi]
    is_yang = ri_gan in "甲丙戊庚壬"
    divisor = 9 if is_yang else 6
    remainder = total % divisor or divisor

    # 6. 打印输出
    print("\033[1;32m" + "═"*50 + "\033[0m")
    print(f"🕒 时间：{now.strftime('%Y-%m-%d %H:%M')}")
    print(f"🏮 干支：{ri_gan_zhi}日 {shi_gan_zhi}时 ({'阳日' if is_yang else '阴日'})")
    print("\033[1;32m" + "─"*50 + "\033[0m")
    
    if remainder == 5:
        print("💡 \033[1;33m对应卦象：中宫 (5)\033[0m")
        print("👉 \033[1;31m男取：后溪 (兑)\033[0m -> 握拳，小指掌指关节后肉际处")
        print("👉 \033[1;31m女取：列缺 (离)\033[0m -> 桡骨茎突上方，两手虎口交叉食指尽处")
    else:
        gua, point, pos, mai, match, match_pos = bafa_data[remainder]
        print(f"💡 对应卦象：\033[1;35m{gua}卦\033[0m")
        print(f"🎯 主开穴位：\033[1;31m{point}\033[0m (通{mai})")
        print(f"📍 定位提示：{pos}")
        print("-" * 20)
        print(f"🔗 建议配穴：\033[1;36m{match}\033[0m")
        print(f"📍 定位提示：{match_pos}")
    print("\033[1;32m" + "═"*50 + "\033[0m")

if __name__ == "__main__":
    get_realtime_bafa()
    print('''公孙配内关：主治心、胸、胃部疾病。
后溪配申脉：主治目内眦、颈项、耳、肩膊、小肠、膀胱疾病。
外关配临泣：主治目外眦、耳后、颊、颈肩疾病。
列缺配照海：主治喉咙、胸膈、肺部疾病。''')
