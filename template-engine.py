#!/usr/bin/env python3

template_engine = {
    "stamps/small-jp-en": {
        "template_prefix": "stamp",
        "template_file_names": ["horizontal", "vertical"],
        "template_field_names":         ["EN_LABEL",              "JP_LABEL"            ],
        "template_dataset": [
            ("arm-left",                ["LEFT ARM",              "左腕"                ]),
            ("arm-right",               ["RIGHT ARM",             "右腕"                ]),
            ("arm",                     ["ARM",                   "腕"                  ]),
            ("assortment-match",        ["ASSORTMENT MATCH",      "組み合わせ"          ]),
            ("back-side",               ["BACK SIDE",             "裏"                  ]),
            ("back",                    ["BACK",                  "後"                  ]),
            ("badge",                   ["BADGE",                 "バッチ"              ]),
            ("bag",                     ["BAG",                   "バッグ"              ]),
            ("balance-comp",            ["BALANCE COMP",          "他〜と合成"          ]),
            ("balance-do-t",            ["BALANCE DOⓉ",          "他〜を同トレス"      ]),
            ("balance-t",               ["BALANCEⓉ",             "他〜をトレス"        ]),
            ("balance",                 ["BALANCE",               "残りの部分"          ]),
            ("beam",                    ["BEAM",                  "ビーム"              ]),
            ("beard",                   ["BEARD",                 "髭"                  ]),
            ("belt-buckle",             ["BELT BUCKLE",           "バックル"            ]),
            ("belt",                    ["BELT",                  "ベルト"              ]),
            ("bg-video",                ["BG VIDEO",              "環境映像"            ]),
            ("bl-efx",                  ["BL EFX",                "透過光"              ]),
            ("blink-action",            ["BLINK ACTION",          "中目パチ"            ]),
            ("blood",                   ["BLOOD",                 "血"                  ]),
            ("blouse",                  ["BLOUSE",                "ブラウス"            ]),
            ("bluish-paint",            ["BLUISH PAINT",          "ブルートーン彩色"    ]),
            ("bokeh",                   ["BOKEH",                 "ボケ"                ]),
            ("brush-air",               ["AIR BRUSH",             "エアーブラシ"        ]),
            ("brush-dry",               ["DRY BRUSH",             "ドライブラシ"        ]),
            ("brush",                   ["BRUSH",                 "ブラシ"              ]),
            ("bure",                    ["BURE",                  "ブレ"                ]),
            ("button",                  ["BUTTON",                "バタン"              ]),
            ("cel-bank",                ["BANK CEL",              "バンクセル"          ]),
            ("cel-correction",          ["CORRECTION CEL",        "かぶせセル"          ]),
            ("cel-hanken",              ["HANKEN CEL",            "版権セル"            ]),
            ("cel-large",               ["LARGE CEL",             "大判セル"            ]),
            ("cel-long",                ["LONG CEL",              "長セル"              ]),
            ("cel-only",                ["ONLY CEL",              "全セル"              ]),
            ("cel-separate-wxp",        ["SEPARATE WXP CEL",      "WXP別セル"           ]),
            ("cel-separate",            ["SEPARATE CEL",          "別セル"              ]),
            ("character-guest",         ["GUEST CHARACTER",       "ゲストキャラクター"  ]),
            ("character-main",          ["MAIN CHARACTER",        "マインキャラクター"  ]),
            ("check-harding",           ["HARDING CHECK",         "ハーディングチェック"]),
            ("check-paka-paka",         ["PAKA-PAKA CHECK",       "パカパカチェック"    ]),
            ("check-pokemon",           ["POKÉMON CHECK",         "ポケモンチェック"    ]),
            ("cleaning",                ["CLEANING",              "消し込み"            ]),
            ("clear",                   ["CLEAR",                 "ヌキ"                ]),
            ("close-up",                ["CLOSE UP",              "クローズアップ"      ]),
            ("clothes-autumn",          ["AUTUMN",                "秋服"                ]),
            ("clothes-spring",          ["SPRING",                "春服"                ]),
            ("clothes-summer",          ["SUMMER",                "夏服"                ]),
            ("clothes-winter",          ["WINTER",                "冬服"                ]),
            ("clothes",                 ["CLOTHES",               "服"                  ]),
            ("cloud",                   ["CLOUD",                 "雲"                  ]),
            ("coat",                    ["COAT",                  "コート"              ]),
            ("collar",                  ["COLLAR",                "カラー"              ]),
            ("color-chart",             ["COLOR CHART",           "カラーチャート"      ]),
            ("color-ht",                ["COLOR H.Ⓣ",            "色トレス"            ]),
            ("com-ng",                  ["COM. NG",               "合成不可"            ]),
            ("come-in-this",            ["COME IN THIS",          "これでIN"            ]),
            ("compositor",              ["COMPOSITOR",            "撮影"                ]),
            ("compound",                ["COMPOUND",              "合成"                ]),
            ("costume",                 ["COSTUME",               "コスチューム"        ]),
            ("cross-section",           ["CROSS SECTION",         "断面"                ]),
            ("crotch-line",             ["CROTCH LINE",           "股下ライン"          ]),
            ("cut-back",                ["CUT BACK",              "カットバック"        ]),
            ("cut-in",                  ["CUT IN",                "カットイン"          ]),
            ("cut-insert",              ["INSERT CUT",            "インサートカット"    ]),
            ("cut",                     ["CUT",                   "カット"              ]),
            ("day",                     ["DAY",                   "昼"                  ]),
            ("designer",                ["DESIGNER",              "デザイナー"          ]),
            ("dial-com",                ["DIAL.COM",              "セリフ合成"          ]),
            ("disuse-shadow",           ["DISUSE SHADOW",         "カゲ不要"            ]),
            ("done",                    ["DONE",                  "アップ"              ]),
            ("draft",                   ["DRAFT",                 "ドラフト"            ]),
            ("earring-1",               ["EARRING",               "イヤリング"          ]),
            ("earring-2",               ["EARRING",               "ピアス"              ]),
            ("effects-special",         ["SPECIAL EFFECTS",       "特殊効果"            ]),
            ("end",                     ["END",                   "止"                  ]),
            ("evening-color",           ["EVENING COLOR",         "夕景彩色"            ]),
            ("expression",              ["EXPRESSION",            "表情"                ]),
            ("eye-half-open",           ["HALF OPEN EYE",         "半分開き目"          ]),
            ("eye-open",                ["OPEN EYE",              "開きめ"              ]),
            ("eye-white",               ["WHITE OF EYE",          "白目"                ]),
            ("eye",                     ["EYE",                   "目"                  ]),
            ("eyebrow",                 ["EYEBROW",               "眉"                  ]),
            ("eyes-closed-1",           ["CLOSED EYES",           "閉目"                ]),
            ("eyes-closed-2",           ["CLOSED EYES",           "とじ目"              ]),
            ("eyes-middle",             ["MIDDLE EYES",           "中目"                ]),
            ("eyeshadow",               ["EYESHADOW",             "アイシャドー"        ]),
            ("face",                    ["FACE",                  "顔"                  ]),
            ("fade-in",                 ["FADE IN",               "フェードイン"        ]),
            ("fade-out",                ["FADE OUT",              "フェードアウト"      ]),
            ("fairing",                 ["FAIRING",               "フェアリング"        ]),
            ("finger",                  ["FINGER",                "ゆび"                ]),
            ("fire",                    ["FIRE",                  "火"                  ]),
            ("fix",                     ["FIX",                   "フィックス"          ]),
            ("flare",                   ["FLARE",                 "フレア"              ]),
            ("flicker",                 ["FLICKER",               "フリッカー"          ]),
            ("focus-in",                ["FOCUS IN",              "フォークスイン"      ]),
            ("focus-out",               ["FOCUS OUT",             "フォークスアウト"    ]),
            ("focus",                   ["FOCUS",                 "フォークス"          ]),
            ("follow",                  ["FOLLOW",                "フォロー"            ]),
            ("foot-left",               ["LEFT FOOT",             "左足"                ]),
            ("foot-right",              ["RIGHT FOOT",            "右足"                ]),
            ("foot",                    ["FOOT",                  "足"                  ]),
            ("forest",                  ["FOREST",                "森"                  ]),
            ("frame-in",                ["FRAME IN",              "フレームイン"        ]),
            ("frame-out",               ["FRAME OUT",             "フレームアウト"      ]),
            ("frame",                   ["FRAME",                 "フレーム"            ]),
            ("free-coloring",           ["FREE COLORING",         "自由彩色"            ]),
            ("frills",                  ["FRILLS",                "フリル"              ]),
            ("front",                   ["FRONT",                 "前"                  ]),
            ("gengaman",                ["GENGAMAN",              "原画"                ]),
            ("gensatsu-finished",       ["GENSATSU FINISHED",     "原撮済"              ]),
            ("glasses",                 ["GLASSES",               "ガラス"              ]),
            ("gloves",                  ["GLOVES",                "手袋"                ]),
            ("grayscale",               ["GRAYSCALE",             "グレースケール"      ]),
            ("ground-shadow",           ["GROUND SHADOW",         "地面の影"            ]),
            ("hair",                    ["HAIR",                  "髪"                  ]),
            ("hand-left",               ["LEFT HAND",             "左手"                ]),
            ("hand-right",              ["RIGHT HAND",            "右手"                ]),
            ("hand",                    ["HAND",                  "手"                  ]),
            ("hat",                     ["HAT",                   "帽子"                ]),
            ("held",                    ["HELD",                  "止め"                ]),
            ("high-contrast",           ["HIGH CONTRAST",         "ハイコントラスト"    ]),
            ("highlight",               ["HIGHLIGHT",             "HIライト"            ]),
            ("in-between",              ["IN-BETWEEN",            "動画"                ]),
            ("iris",                    ["IRIS",                  "虹彩"                ]),
            ("jacket",                  ["JACKET",                "ジャケット"          ]),
            ("jaw-line",                ["JAW LINE",              "顎ライン"            ]),
            ("jeans",                   ["JEANS",                 "ジーンズ"            ]),
            ("kakikomi",                ["KAKIKOMI",              "〜に描き込み"        ]),
            ("key-animation",           ["KEY ANIMATION",         "原画"                ]),
            ("kneesocks",               ["KNEESOCKS",             "ニーソックス"        ]),
            ("kumi-new",                ["MATCH LINE",            "〜とクミ"            ]),
            ("kumi-old",                ["REG. TO",               "〜と組合せ"          ]),
            ("layer",                   ["LAYER",                 "レイヤー"            ]),
            ("layout",                  ["LAYOUT",                "レイアウト"          ]),
            ("left",                    ["LEFT",                  "左"                  ]),
            ("leg-left",                ["LEFT LEG",              "左脚"                ]),
            ("leg-right",               ["RIGHT LEG",             "右脚"                ]),
            ("leg",                     ["LEG",                   "脚"                  ]),
            ("lens-flare",              ["LENS FLARE",            "レンズフレア"        ]),
            ("lens-ghost",              ["LENS GHOST",            "レンズゴースト"      ]),
            ("lettering",               ["LETTERING",             "レタリング"          ]),
            ("light-catch",             ["CATCH LIGHT",           "キャッチライト"      ]),
            ("light-counter",           ["COUNTER LIGHT",         "逆光"                ]),
            ("light-fill",              ["FILL LIGHT",            "補助光"              ]),
            ("light-key",               ["KEY LIGHT",             "主光線"              ]),
            ("light-line",              ["LINE LIGHT",            "ラインライト"        ]),
            ("light-main",              ["MAIN LIGHT",            "マインライト"        ]),
            ("light-top",               ["TOP LIGHT",             "トップライト"        ]),
            ("light",                   ["LIGHT",                 "光"                  ]),
            ("lip-lower",               ["LOWER LIP",             "下唇"                ]),
            ("lip-synch",               ["LIP SYNCH",             "セリフ"              ]),
            ("lip-upper",               ["UPPER LIP",             "上唇"                ]),
            ("lip",                     ["LIP",                   "唇"                  ]),
            ("lipstick",                ["LIPSTICK",              "口紅"                ]),
            ("loop",                    ["LOOP",                  "ループ"              ]),
            ("ls-action",               ["L.S. ACTION",           "中割り口パク"        ]),
            ("ls-covers",               ["L.S. COVERS",           "セリフかぶせ"        ]),
            ("man",                     ["MAN",                   "男"                  ]),
            ("mask-back-bl",            ["BACK BL MASK",          "ウラBLヌリ"          ]),
            ("mask-bl-efx",             ["BL EFX MASK",           "透過光マスク"        ]),
            ("mask-clear",              ["CLEAR MASK",            "ヌキマスク"          ]),
            ("mask-female",             ["FEMALE MASK",           "メスマスク"          ]),
            ("mask-male",               ["MALE MASK",             "オスマスク"          ]),
            ("match-color-with",        ["MATCH COLOR WITH 〜",   "〜と色合わせ"        ]),
            ("memo",                    ["MEMO",                  "連絡事項"            ]),
            ("mm-per-frame",            ["MM/FRAME",              "ミリ/K"              ]),
            ("monochrome",              ["MONOCHROME",            "モノクローム"        ]),
            ("monotone",                ["MONOTONE",              "モノトーン"          ]),
            ("motion-blur",             ["MOTION BLUR",           "モションブラ"        ]),
            ("mouth-closed",            ["CLOSED MOUTH",          "閉口"                ]),
            ("mouth-inside",            ["INSIDE OF MOUTH",       "口の中"              ]),
            ("mouth-middle",            ["MIDDLE MOUTH",          "中口"                ]),
            ("mouth-open",              ["OPEN MOUTH",            "開け口"              ]),
            ("nail",                    ["NAIL",                  "爪"                  ]),
            ("neck",                    ["NECK",                  "首"                  ]),
            ("necklace",                ["NECKLACE",              "ネックレス"          ]),
            ("necktie",                 ["NECKTIE",               "ネクタイ"            ]),
            ("night",                   ["NIGHT",                 "夜色"                ]),
            ("nipples",                 ["NIPPLES",               "乳首"                ]),
            ("no-need",                 ["NO NEED",               "不要"                ]),
            ("no-shadow-for-balance",   ["NO SHADOW FOR BALANCE", "他影不要"            ]),
            ("none",                    ["NONE",                  "なし"                ]),
            ("normal-color-1",          ["NORMAL COLOR",          "ノーマル"            ]),
            ("normal-color-2",          ["NORMAL COLOR",          "ノーマルカラー"      ]),
            ("normal",                  ["NORMAL",                "ノーマル"            ]),
            ("nose",                    ["NOSE",                  "鼻"                  ]),
            ("off-scene",               ["OFF SCENE",             "オフシーン"          ]),
            ("offset",                  ["OFFSET",                "オフセット"          ]),
            ("one-tone-darker-1",       ["1 TONE DARKER",         "ノーマル段カゲ"      ]),
            ("one-tone-darker-2",       ["1 TONE DARKER",         "影１段落とし"        ]),
            ("one-tone-lighter",        ["1 TONE LIGHTER",        "ノーマル一段上げ"    ]),
            ("overlap",                 ["OVERLAP",               "オーバーラップ"      ]),
            ("overlay",                 ["OVERLAY",               "BOOK上"              ]),
            ("p-to-edge",               ["Ⓟ TO EDGE",            "セルバレ注意"        ]),
            ("p-whole-frame",           ["Ⓟ WHOLE FRAME",        "全面塗り"            ]),
            ("paint-1",                 ["Ⓟ",                    "ペイント"            ]),
            ("paint-2",                 ["PAINT",                 "ペイント"            ]),
            ("paint-reference",         ["PAINT REFERENCE",       "塗り分け参考"        ]),
            ("pan-focus",               ["PAN-FOCUS",             "パンフォークス"      ]),
            ("pan-follow",              ["FOLLOW PAN",            "フォローパン"        ]),
            ("pan-memori",              ["MEMORI PAN",            "目盛りパン"          ]),
            ("pan-rapid",               ["RAPID PAN",             "流パン"              ]),
            ("pan-tsuke",               ["TSUKE PAN",             "つけパン"            ]),
            ("pan",                     ["PAN",                   "パン"                ]),
            ("parallax",                ["PARALLAX",              "パララックス"        ]),
            ("part-a",                  ["A-PART",                "Aパート"             ]),
            ("part-b",                  ["B-PART",                "Bパート"             ]),
            ("patterns",                ["PATTERNS",              "模様"                ]),
            ("peg-bottom",              ["BOTTOM PEG",            "下タップ"            ]),
            ("peg-top-and-bottom",      ["TOP&BOTTOM PEG",        "上下タップ"          ]),
            ("peg-top",                 ["TOP PEG",               "上タップ"            ]),
            ("pendant",                 ["PENDANT",               "ペンダント"          ]),
            ("pixel-art",               ["PIXEL ART",             "ドット絵"            ]),
            ("preview",                 ["PREVIEW",               "プレビュー"          ]),
            ("pull",                    ["PULL",                  "引き"                ]),
            ("pupil",                   ["PUPIL",                 "瞳"                  ]),
            ("rack-focus-back",         ["BACK",                  "後ピン"              ]),
            ("rack-focus-front",        ["FRONT",                 "前ピン"              ]),
            ("rack-focus",              ["RACK FOCUS",            "ピン送り"            ]),
            ("rain",                    ["RAIN",                  "雨"                  ]),
            ("reference",               ["REFERENCE",             "参考"                ]),
            ("repeat",                  ["REPEAT",                "リピート"            ]),
            ("replace-bg",              ["BG REPLACEMENT",        "BG置き換え"          ]),
            ("replace-book",            ["BOOK REPLACEMENT",      "BOOK置き換え"        ]),
            ("reverse-erase",           ["REVERSE ERASE",         "逆消し込み"          ]),
            ("reverse-use",             ["REVERSE USE",           "逆シート"            ]),
            ("ribbon",                  ["RIBBON",                "リボン"              ]),
            ("right",                   ["RIGHT",                 "右"                  ]),
            ("rolling",                 ["ROLLING",               "ローリング"          ]),
            ("rotoscope",               ["ROTOSCOPE",             "ロトスコープ"        ]),
            ("scarf",                   ["SCARF",                 "スカーフ"            ]),
            ("scene",                   ["SCENE",                 "シーン"              ]),
            ("settei-art",              ["ART SETTING",           "美術設定"            ]),
            ("settei-basic",            ["BASIC SETTING",         "基本設定"            ]),
            ("settei-character",        ["CHARACTER SETTING",     "キャラクター設定"    ]),
            ("settei-guest",            ["GUEST SETTING",         "ゲスト設定"          ]),
            ("settei-prop",             ["PROP SETTING",          "プロップ設定"        ]),
            ("settei",                  ["SETTING",               "設定"                ]),
            ("shadow-1",                ["SHADOW",                "カゲ"                ]),
            ("shadow-2",                ["SHADOW",                "カゲ有り"            ]),
            ("shadow-for-only",         ["SHADOW FOR ONLY 〜",    "〜のみ影あり"        ]),
            ("shadow-one",              ["SHADOW 1",              "一号影"              ]),
            ("shadow-three-darker",     ["SHADOW 3 DARKER",       "影３段落とし"        ]),
            ("shadow-two-darker",       ["SHADOW 2 DARKER",       "影２段落とし"        ]),
            ("shadow-two",              ["SHADOW 2",              "二号影"              ]),
            ("shirt",                   ["SHIRT",                 "シャツ"              ]),
            ("shoe-sole",               ["SHOE SOLE",             "靴裏"                ]),
            ("shoe",                    ["SHOE",                  "靴"                  ]),
            ("shoulder-left",           ["LEFT SHOULDER",         "左肩"                ]),
            ("shoulder-right",          ["RIGHT SHOULDER",        "右肩"                ]),
            ("shoulder",                ["SHOULDER",              "肩"                  ]),
            ("side-back",               ["BACK SIDE",             "後ろ"                ]),
            ("side-bottom",             ["BOTTOM SIDE",           "下面"                ]),
            ("side-front",              ["FRONT SIDE",            "正面"                ]),
            ("side-top",                ["TOP SIDE",              "上面"                ]),
            ("side",                    ["SIDE",                  "側面"                ]),
            ("silhouette",              ["SILHOUETTE",            "シルエット"          ]),
            ("size",                    ["SIZE",                  "サイズ"              ]),
            ("skin",                    ["SKIN",                  "肌"                  ]),
            ("skirt",                   ["SKIRT",                 "スカート"            ]),
            ("sky-blue",                ["BLUE SKY",              "青空"                ]),
            ("sky-evening",             ["EVENING SKY",           "夕空"                ]),
            ("sky-morning",             ["MORNING SKY",           "朝空"                ]),
            ("sky-night",               ["NIGHT SKY",             "夜空"                ]),
            ("sky-rainy",               ["RAINY SKY",             "雨空"                ]),
            ("sky-starry",              ["STARRY SKY",            "星空"                ]),
            ("sky",                     ["SKY",                   "空"                  ]),
            ("slide",                   ["SLIDE",                 "スライド"            ]),
            ("smear",                   ["SMEAR",                 "スミア"              ]),
            ("smoke",                   ["SMOKE",                 "煙"                  ]),
            ("socks-1",                 ["SOCKS",                 "靴下"                ]),
            ("socks-2",                 ["SOCKS",                 "くつした"            ]),
            ("speedline-bg",            ["SPEEDLINE BG",          "流背"                ]),
            ("stage-left",              ["STAGE LEFT",            "上手"                ]),
            ("stage-right",             ["STAGE RIGHT",           "下手"                ]),
            ("status",                  ["STATUS",                "ステータス"          ]),
            ("steam",                   ["STEAM",                 "湯気"                ]),
            ("stocking",                ["STOCKING",              "ストッキング"        ]),
            ("storyboard",              ["STORYBOARD",            "絵コンテ"            ]),
            ("string",                  ["STRING",                "紐"                  ]),
            ("strobe-fx",               ["STROBE FX",             "ストロボ効果"        ]),
            ("suit",                    ["SUIT",                  "スーツ"              ]),
            ("sweat",                   ["SWEAT",                 "汗"                  ]),
            ("swimsuit",                ["SWIMSUIT",              "水着"                ]),
            ("symmetry",                ["SYMMETRY",              "シンメトリー"        ]),
            ("tan-out",                 ["TAN OUT",               "なめ出し"            ]),
            ("tears",                   ["TEARS",                 "涙"                  ]),
            ("teeth",                   ["TEETH",                 "歯"                  ]),
            ("temporary",               ["TEMPORARY",             "仮"                  ]),
            ("text",                    ["TEXT",                  "テキスト"            ]),
            ("tilt",                    ["TILT",                  "チルト"              ]),
            ("time-sheet",              ["TIME SHEET",            "タイムシート"        ]),
            ("timing-sheet",            ["TIMING SHEET",          "タイムシート"        ]),
            ("timing",                  ["TIMING",                "タイミング"          ]),
            ("title",                   ["TITLE",                 "タイトル"            ]),
            ("tojikuchi-k",             ["TOJIKUCHI K.",          "閉じ口描き込み"      ]),
            ("tongue",                  ["TONGUE",                "舌"                  ]),
            ("touch",                   ["TOUCH",                 "タッチ"              ]),
            ("trace-1",                 ["Ⓣ",                    "トレス"              ]),
            ("trace-2",                 ["TRACE",                 "トレス"              ]),
            ("trace-color",             ["TRACE COLOR",           "実線色"              ]),
            ("track-back",              ["TRACK BACK",            "トラックバック"      ]),
            ("track-up",                ["TRACK UP",              "トラックアップ"      ]),
            ("translation",             ["TRANSLATION",           "翻訳"                ]),
            ("tree",                    ["TREE",                  "木"                  ]),
            ("underlay",                ["UNDERLAY",              "BOOK下"              ]),
            ("underlight-bg",           ["BG UNDERLIGHT",         "BGT光"               ]),
            ("underlight-cross",        ["CROSS UNDERLIGHT",      "クロスT光"           ]),
            ("underlight",              ["UNDERLIGHT",            "T光"                 ]),
            ("underwear",               ["UNDERWEAR",             "パンツ"              ]),
            ("uniform-1",               ["UNIFORM",               "ユニフォーム"        ]),
            ("uniform-2",               ["UNIFORM",               "校服"                ]),
            ("up-and-down-action",      ["UP/DOWN ACTION",        "(動きに)山をつける"  ]),
            ("view-birds-eye",          ["BIRD'S-EYE VIEW",       "俯瞰"                ]),
            ("view-eye-level",          ["EYE LEVEL VIEW",        "めだか"              ]),
            ("view-worms-eye",          ["WORM'S-EYE VIEW",       "あおり"              ]),
            ("wall",                    ["WALL",                  "かべ"                ]),
            ("water",                   ["WATER",                 "水"                  ]),
            ("wave-glass",              ["WAVE GLASS",            "波ガラス"            ]),
            ("wide-angle",              ["WIDE ANGLE",            "広角"                ]),
            ("wings",                   ["WINGS",                 "翼"                  ]),
            ("wipe-in",                 ["WIPE IN",               "ワイプイン"          ]),
            ("wipe-out",                ["WIPE OUT",              "ワイプアウト"        ]),
            ("woman",                   ["WOMAN",                 "女"                  ]),
            ("wraparound-shot",         ["WRAPAROUND SHOT",       "回り込み"            ]),
            ("zoom-cut-in",             ["ZOOM CUT IN",           "ポン寄り"            ]),
            ("zoom-cut-out",            ["ZOOM CUT OUT",          "ポン引き"            ]),
        ],
    },
    "stamps/large-jp": {
        "template_prefix": "stamp",
        "template_file_names": ["horizontal", "vertical"],
        "template_field_names":                   ["JP_LABEL",         "576"],
        "template_dataset": [
            ("character-relationship",            ["キャラクタ関係図", "410"]),
            ("clean-copy",                        ["清書",             "110"]),
            ("color-design",                      ["色彩設計",         "210"]),
            ("comparison",                        ["对比",             "110"]),
            ("completed-drawing",                 ["完成図",           "160"]),
            ("confidential",                      ["社外秘",           "160"]),
            ("douga-collection",                  ["動画集",           "160"]),
            ("draft-final",                       ["決定稿",           "160"]),
            ("draft-preliminary",                 ["準備稿",           "160"]),
            ("gensatsu-finished",                 ["原撮済",           "160"]),
            ("jun-kumi",                          ["準クミ",           "160"]),
            ("keyframe-1",                        ["原画",             "110"]),
            ("keyframe-rough",                    ["ラフ原画",         "210"]),
            ("layout-1",                          ["レイアウト",       "250"]),
            ("layout-2",                          ["原図",             "110"]),
            ("page-x",                            ["PAGE　　",         "200"]),
            ("pending-approval",                  ["監修中",           "160"]),
            ("prohibited-reproduction",           ["無断転載禁止",     "310"]),
            ("reference",                         ["参考",             "110"]),
            ("revision-animation-director",       ["作監修正",         "210"]),
            ("revision-character-director",       ["キャラデ修正",     "310"]),
            ("revision-chief-animation-director", ["総作監修正",       "260"]),
            ("revision-episode-director",         ["演出修正",         "210"]),
            ("revision-series-director",          ["監督修正",         "210"]),
            ("revision",                          ["修正",             "110"]),
            ("scan-required",                     ["要SCAN",           "190"]),
            ("settei-collection",                 ["設定資料集",       "260"]),
            ("settei",                            ["設定",             "110"]),
            ("submitted",                         ["原図出済",         "210"]),
            ("urgent",                            ["至急",             "110"]),
        ],
    }
}

import os

for (template_base_directory, template) in template_engine.items():
    for template_file_name in template["template_file_names"]:
        os.makedirs(
            "{}/{}".format(
                template_base_directory,
                template_file_name,
            ),
            exist_ok = True,
        )

        template_svg_path = "{}/.templates/template-{}.svg".format(
            template_base_directory,
            template_file_name,
        )

        with open(template_svg_path, "r") as template_svg_file:
            template_svg_data = template_svg_file.read()

        for (instance_name, instance_data) in template["template_dataset"]:
            instance_svg_data = template_svg_data
            for (a, b) in zip(template["template_field_names"], instance_data):
                instance_svg_data = instance_svg_data.replace(a, b.replace("&", "&amp;"))

            instance_svg_path = "{}/{}/{}-{}.svg".format(
                template_base_directory,
                template_file_name,
                template["template_prefix"],
                instance_name
            )

            with open(instance_svg_path, "w") as instance_svg_file:
                instance_svg_file.write(instance_svg_data)
