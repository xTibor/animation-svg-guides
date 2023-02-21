#!/usr/bin/env python3

stamp_definitions = [
    ("balance-do-t",             "BALANCE DOⓉ",             "他〜を同トレス"       ),
    ("balance-t",                "BALANCEⓉ",                "他〜をトレス"         ),
    ("balance",                  "BALANCE",                  "残りの部分"           ),
    ("blink-action",             "BLINK ACTION",             "中目パチ"             ),
    ("brush",                    "BRUSH",                    "ブラシ"               ),
    ("clear",                    "CLEAR",                    "ヌキ"                 ),
    ("clothes",                  "CLOTHES",                  "服"                   ),
    ("disuse-shadow",            "DISUSE SHADOW",            "カゲ不要"             ),
    ("frame",                    "FRAME",                    "フレーム"             ),
    ("ground-shadow",            "GROUND SHADOW",            "地面の影"             ),
    ("hair",                     "HAIR",                     "髪"                   ),
    ("half-open-eye",            "HALF OPEN EYE",            "半分開き目"           ),
    ("high-contrast",            "HIGH CONTRAST",            "ハイコントラスト"     ),
    ("lip-synch",                "LIP SYNCH",                "セリフ"               ),
    ("ls-action",                "L.S.ACTION",               "中割り口パク"         ),
    ("main-character",           "MAIN CHARACTER",           "マインキャラクター"   ),
    ("no-shadow-for-balance",    "NO SHADOW FOR BALANCE",    "他影不要"             ),
    ("normal-color-1",           "NORMAL COLOR",             "ノーマル"             ),
    ("normal-color-2",           "NORMAL COLOR",             "ノーマルカラー"       ),
    ("one-tone-darker-1",        "1 TONE DARKER",            "ノーマル段カゲ"       ),
    ("one-tone-darker-2",        "1 TONE DARKER",            "影１段落とし"         ),
    ("open-eye",                 "OPEN EYE",                 "開きめ"               ),
    ("open-mouth",               "OPEN MOUTH",               "開け口"               ),
    ("reg-to",                   "REG. TO",                  "〜と組合せ"           ),
    ("shadow-1",                 "SHADOW",                   "カゲ"                 ),
    ("shadow-2",                 "SHADOW",                   "カゲ有り"             ),
    ("shadow-for-only",          "SHADOW FOR ONLY 〜",       "〜のみ影あり"         ),
    ("shadow-two-darker",        "SHADOW 2 DARKER",          "影２段落とし"         ),
    ("skin",                     "SKIN",                     "肌"                   ),
    ("slide",                    "SLIDE",                    "スライド"             ),
    ("sweat",                    "SWEAT",                    "汗"                   ),
    ("tears",                    "TEARS",                    "涙"                   ),
    ("touch",                    "TOUCH",                    "タッチ"               ),
]

stamp_templates = [
    ("horizontal",  "stamp-template-horizontal.svg" ),
    ("vertical",    "stamp-template-vertical.svg"   ),
]

for stamp_template_name, stamp_template_path in stamp_templates:
    with open(stamp_template_path, "r") as stamp_template_file:
        stamp_template_data = stamp_template_file.read()

    for base_name, en_label, jp_label in stamp_definitions:
        with open("{}/stamp-{}.svg".format(stamp_template_name, base_name), "w") as stamp_file:
            stamp_file.write(
                stamp_template_data
                    .replace("JP_LABEL", jp_label)
                    .replace("EN_LABEL", en_label)
            )
