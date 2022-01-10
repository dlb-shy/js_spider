# encoding = utf-8
import json
import time
from pprint import pprint
import cv2
import numpy as np

import pyDes
import base64

import requests
traces = {51:
              [[0, 0, 1]
                  , [3, -3, 112]
                  , [40, -11, 203]
                  , [59, -15, 301]
                  , [65, -15, 401]
                  , [65, -15, 501]
                  , [65, -15, 602]
                  , [61, -15, 704]
                  , [54, -14, 803]
                  , [51, -12, 901]
                  , [51, -12, 1002]
                  , [51, -12, 1102]
                  , [51, -12, 1201]
               ],

          53: [
              [0, 0, 0]
              , [11, -2, 100]
              , [27, -5, 201]
              , [38, -7, 301]
              , [45, -7, 413]
              , [45, -7, 508]
              , [47, -7, 602]
              , [50, -8, 705]
              , [52, -8, 811]
              , [53, -9, 912]
          ],

          61: [
              [0, 0, 0]
              , [4, 0, 100]
              , [32, -3, 200]
              , [43, -6, 300]
              , [48, -7, 400]
              , [54, -8, 501]
              , [60, -9, 601]
              , [61, -10, 701]
              , [61, -10, 806]
          ],

          65: [
              [0, -4, 0]
              , [4, -1, 102]
              , [37, -11, 200]
              , [62, -19, 301]
              , [68, -21, 401]
              , [70, -21, 510]
              , [70, -21, 603]
              , [70, -21, 711]
              , [68, -21, 801]
              , [63, -20, 900]
              , [61, -19, 1001]
              , [61, -19, 1114]
              , [61, -19, 1208]
              , [61, -19, 1303]
              , [61, -19, 1413]
              , [62, -19, 1505]
              , [65, -20, 1601]
              , [65, -20, 1708]
              , [65, -20, 1801]
              , [65, -20, 1910]
              , [65, -20, 2003]
              , [65, -20, 2112]
          ],
          68: [
              [0, -1, 0]
              , [5, 0, 101]
              , [25, -6, 200]
              , [41, -9, 301]
              , [60, -10, 404]
              , [65, -10, 508]
              , [65, -10, 601]
              , [65, -10, 711]
              , [67, -10, 801]
              , [68, -10, 901]
              , [68, -10, 1008]
              , [68, -10, 1101]
          ],

          74: [
              [0, 2, 0]
              , [6, -1, 100]
              , [23, -4, 201]
              , [40, -2, 301]
              , [51, 0, 400]
              , [62, 2, 502]
              , [69, 3, 601]
              , [73, 4, 701]
              , [74, 4, 813]
              , [74, 4, 906]
              , [74, 4, 1015]
          ],

          80: [
              [0, 0, 0]
              , [30, -7, 108]
              , [46, -10, 201]
              , [59, -11, 306]
              , [70, -12, 403]
              , [74, -12, 501]
              , [78, -14, 607]
              , [80, -14, 701]
              , [80, -14, 802]
              , [80, -14, 901]
          ],

          88: [
              [0, 0, 0]
              , [2, -1, 100]
              , [37, -1, 201]
              , [58, 2, 301]
              , [75, 2, 401]
              , [79, 2, 501]
              , [82, 2, 611]
              , [82, 1, 705]
              , [87, 1, 818]
              , [88, 0, 903]
              , [88, 0, 1003]
              , [88, 0, 1118]
          ],

          90: [
              [0, 0, 0]
              , [9, 1, 101]
              , [36, -4, 201]
              , [58, -9, 300]
              , [73, -9, 400]
              , [79, -6, 500]
              , [83, -7, 601]
              , [86, -7, 700]
              , [89, -7, 800]
              , [89, -7, 911]
              , [90, -7, 1005]
              , [90, -7, 1115]

          ],

          92: [
              [0, -5, 0]
              , [1, 0, 115]
              , [30, -8, 202]
              , [47, -13, 301]
              , [63, -18, 402]
              , [76, -21, 501]
              , [83, -23, 602]
              , [85, -23, 708]
              , [87, -24, 800]
              , [88, -25, 901]
              , [90, -26, 1001]
              , [92, -26, 1100]
              , [92, -26, 1203]
              , [92, -26, 1312]
          ],

          96: [
              [0, 3, 0]
              , [4, 0, 102]
              , [24, -7, 202]
              , [46, -13, 304]
              , [53, -14, 402]
              , [66, -16, 501]
              , [75, -16, 601]
              , [83, -15, 702]
              , [88, -13, 802]
              , [91, -12, 901]
              , [93, -11, 1001]
              , [96, -10, 1101]
              , [96, -10, 1209]
              , [96, -10, 1302]
          ],

          99: [
              [0, 0, 0]
              , [0, 0, 114]
              , [13, -4, 203]
              , [32, -8, 302]
              , [78, -9, 401]
              , [92, -12, 501]
              , [101, -12, 601]
              , [102, -12, 701]
              , [102, -12, 802]
              , [102, -12, 908]
              , [101, -12, 1001]
              , [99, -12, 1102]
              , [99, -12, 1202]
              , [99, -12, 1311]

          ],

          103: [
              [0, 0, 1]
              , [12, 1, 101]
              , [37, -3, 202]
              , [53, -5, 301]
              , [63, -5, 401]
              , [76, -8, 502]
              , [85, -8, 602]
              , [91, -7, 702]
              , [96, -7, 802]
              , [100, -7, 902]
              , [102, -6, 1012]
              , [102, -6, 1107]
              , [103, -6, 1203]
              , [103, -6, 1309]
              , [103, -6, 1402]
          ],

          106: [
              [0, -2, 0]
              , [8, 2, 103]
              , [42, -6, 201]
              , [71, -8, 302]
              , [83, -8, 401]
              , [90, -8, 501]
              , [94, -8, 601]
              , [98, -8, 701]
              , [101, -9, 804]
              , [105, -9, 901]
              , [106, -9, 1002]
              , [106, -9, 1116]
          ],

          115: [
              [0, 0, 1]
              , [3, 1, 104]
              , [20, -2, 204]
              , [40, -5, 301]
              , [55, -8, 402]
              , [80, -8, 502]
              , [94, -7, 602]
              , [108, -6, 702]
              , [112, -6, 802]
              , [114, -5, 902]
              , [114, -5, 1002]
              , [115, -4, 1102]
              , [115, -4, 1203]
              , [115, -4, 1302]
              , [115, -4, 1401]
              , [115, -4, 1502]
              , [115, -4, 1602]
              , [115, -4, 1702]
          ],

          126: [
              [0, 0, 1]
              , [8, -3, 101]
              , [31, -10, 201]
              , [53, -14, 301]
              , [77, -14, 401]
              , [98, -14, 502]
              , [107, -16, 602]
              , [117, -14, 702]
              , [119, -14, 801]
              , [122, -14, 902]
              , [122, -14, 1003]
              , [122, -14, 1113]
              , [122, -14, 1207]
              , [124, -14, 1301]
              , [126, -14, 1401]
              , [126, -14, 1501]
              , [126, -14, 1610]
          ],

          127: [
              [0, 0, 0]
              , [8, 0, 100]
              , [38, -9, 201]
              , [64, -12, 300]
              , [87, -12, 401]
              , [99, -13, 501]
              , [110, -16, 601]
              , [120, -19, 702]
              , [124, -19, 802]
              , [127, -19, 901]
              , [127, -19, 1001]
              , [127, -19, 1110]
              , [127, -19, 1203]
          ],

          132: [
              [0, -6, 0]
              , [1, 0, 101]
              , [40, 0, 202]
              , [62, -4, 300]
              , [87, -8, 400]
              , [110, -9, 500]
              , [124, -7, 603]
              , [126, -6, 704]
              , [127, -6, 800]
              , [131, -6, 900]
              , [132, -6, 1002]
              , [132, -6, 1111]
              , [132, -6, 1205]
          ],

          140: [
              [0, 1, 0]
              , [1, 0, 101]
              , [29, -11, 201]
              , [58, -11, 301]
              , [90, -13, 401]
              , [107, -13, 502]
              , [115, -13, 601]
              , [123, -14, 701]
              , [128, -14, 801]
              , [132, -14, 901]
              , [135, -16, 1001]
              , [137, -16, 1101]
              , [139, -16, 1201]
              , [140, -15, 1301]
              , [140, -15, 1403]

          ],
          134: [
              [0, 0, 0]
              , [11, -1, 101]
              , [43, 1, 200]
              , [69, 7, 300]
              , [99, 13, 400]
              , [116, 15, 501]
              , [126, 18, 600]
              , [129, 19, 700]
              , [129, 19, 806]
              , [129, 19, 915]
              , [129, 19, 1009]
              , [133, 19, 1102]
              , [134, 19, 1204]
              , [134, 19, 1306]

          ],

          148: [
              [0, 0, 0]
              , [15, -2, 101]
              , [58, -14, 201]
              , [83, -13, 301]
              , [106, -4, 401]
              , [118, -2, 501]
              , [122, -2, 601]
              , [134, -2, 701]
              , [135, -2, 801]
              , [139, -2, 901]
              , [142, -3, 1001]
              , [145, -3, 1101]
              , [146, -4, 1205]
              , [148, -5, 1301]
              , [148, -5, 1408]
              , [148, -5, 1504]
          ],
          153: [
              [0, 1, 0]
              , [36, -7, 101]
              , [67, -12, 201]
              , [102, -17, 302]
              , [117, -17, 401]
              , [130, -18, 502]
              , [140, -20, 601]
              , [143, -20, 701]
              , [147, -21, 810]
              , [149, -21, 904]
              , [149, -21, 1013]
              , [149, -21, 1106]
              , [149, -21, 1215]
              , [151, -21, 1308]
              , [153, -22, 1401]
              , [153, -22, 1513]
              , [153, -22, 1607]
          ],

          154: [
              [0, 0, 0]
              , [17, -6, 101]
              , [58, -8, 201]
              , [93, -14, 300]
              , [125, -12, 401]
              , [137, -12, 505]
              , [145, -12, 601]
              , [150, -12, 701]
              , [152, -12, 800]
              , [154, -12, 901]
              , [154, -12, 1003]
              , [154, -12, 1112]
              , [154, -12, 1206]

          ],

          163: [
              [0, 0, 0]
              , [17, 0, 102]
              , [58, -3, 201]
              , [90, -3, 302]
              , [105, -3, 401]
              , [125, 1, 501]
              , [141, 5, 602]
              , [151, 7, 702]
              , [154, 8, 801]
              , [159, 8, 902]
              , [162, 8, 1001]
              , [163, 8, 1101]
          ],

          166: [
              [0, 0, 0]
              , [7, 0, 102]
              , [75, -12, 201]
              , [111, -14, 301]
              , [122, -18, 402]
              , [131, -21, 501]
              , [142, -21, 601]
              , [148, -21, 701]
              , [153, -21, 801]
              , [158, -22, 902]
              , [159, -22, 1001]
              , [162, -23, 1107]
              , [164, -24, 1201]
              , [165, -24, 1301]
              , [166, -24, 1404]
              , [166, -24, 1514]
              , [166, -24, 1606]

          ],
          174: [
              [0, 0, 0]
              , [6, -2, 102]
              , [20, -8, 202]
              , [60, -18, 300]
              , [79, -19, 401]
              , [105, -19, 500]
              , [133, -22, 601]
              , [159, -22, 700]
              , [170, -22, 801]
              , [174, -22, 901]
              , [174, -22, 1010]
              , [174, -22, 1104]
              , [174, -22, 1214]
              , [174, -22, 1307]

          ],

          178: [
              [0, 0, 0]
              , [0, 0, 110]
              , [17, 0, 203]
              , [72, 6, 304]
              , [110, 13, 401]
              , [134, 7, 505]
              , [153, 5, 611]
              , [162, 5, 701]
              , [166, 5, 800]
              , [168, 5, 902]
              , [170, 4, 1000]
              , [172, 4, 1102]
              , [174, 4, 1214]
              , [175, 4, 1301]
              , [177, 4, 1414]
              , [178, 4, 1516]
              , [178, 4, 1609]
          ],
          186: [
              [0, 0, 0]
              , [4, 1, 102]
              , [27, -2, 201]
              , [44, -5, 300]
              , [101, -14, 401]
              , [134, -14, 501]
              , [156, -17, 602]
              , [171, -20, 702]
              , [174, -21, 801]
              , [176, -22, 901]
              , [179, -23, 1001]
              , [181, -23, 1102]
              , [182, -23, 1203]
              , [185, -24, 1315]
              , [186, -25, 1400]
              , [186, -25, 1514]

          ],
          188: [
              [0, 0, 0]
              , [7, 0, 100]
              , [95, -1, 202]
              , [129, -4, 301]
              , [156, -12, 401]
              , [173, -16, 502]
              , [178, -18, 602]
              , [180, -18, 701]
              , [182, -18, 802]
              , [185, -18, 902]
              , [186, -18, 1001]
              , [186, -18, 1115]
              , [188, -18, 1200]
              , [188, -18, 1301]

          ],

          191: [
              [0, 0, 1]
              , [0, 0, 101]
              , [39, -9, 202]
              , [95, -23, 301]
              , [130, -27, 402]
              , [153, -31, 501]
              , [162, -33, 602]
              , [171, -37, 701]
              , [176, -37, 801]
              , [179, -37, 901]
              , [182, -37, 1001]
              , [183, -38, 1101]
              , [187, -39, 1202]
              , [189, -40, 1310]
              , [191, -40, 1402]
              , [191, -41, 1509]
              , [191, -41, 1604]
              , [191, -41, 1703]

          ],

          189: [
              [0, 0, 0]
              , [22, -4, 100]
              , [67, -19, 202]
              , [110, -23, 301]
              , [146, -17, 401]
              , [153, -15, 501]
              , [162, -14, 602]
              , [172, -15, 701]
              , [176, -15, 801]
              , [179, -15, 901]
              , [183, -15, 1000]
              , [188, -15, 1100]
              , [189, -15, 1201]
              , [189, -15, 1306]
              , [189, -15, 1415]
          ],

          200: [
              [0, 0, 0]
              , [0, 1, 101]
              , [100, 1, 202]
              , [123, 1, 300]
              , [153, -4, 401]
              , [185, -8, 501]
              , [193, -8, 610]
              , [197, -8, 700]
              , [200, -8, 800]
              , [200, -8, 903]
              , [200, -8, 1012]
              , [200, -8, 1107]
          ],

          203: [
              [0, -2, 0]
              , [9, 0, 101]
              , [49, 2, 201]
              , [102, 2, 303]
              , [137, 4, 401]
              , [175, 3, 501]
              , [185, -1, 601]
              , [190, -2, 702]
              , [192, -3, 801]
              , [194, -3, 907]
              , [194, -3, 1003]
              , [197, -3, 1101]
              , [199, -3, 1200]
              , [202, -2, 1300]
              , [203, -2, 1406]
              , [203, -2, 1515]
              , [203, -2, 1609]
          ],
          211: [
              [0, 0, 0]
              , [3, 0, 101]
              , [51, -9, 204]
              , [98, -17, 301]
              , [127, -17, 407]
              , [157, -17, 504]
              , [171, -17, 605]
              , [185, -19, 701]
              , [191, -20, 801]
              , [198, -24, 902]
              , [199, -24, 1013]
              , [202, -25, 1101]
              , [205, -26, 1201]
              , [205, -26, 1309]
              , [205, -26, 1404]
              , [205, -26, 1512]
              , [209, -26, 1605]
              , [211, -26, 1702]
              , [211, -26, 1810]

          ],

          213: [
              [0, 0, 0]
              , [17, 0, 100]
              , [55, -2, 202]
              , [79, -2, 301]
              , [101, -1, 401]
              , [145, -1, 501]
              , [171, 4, 601]
              , [183, 6, 702]
              , [196, 8, 801]
              , [204, 8, 901]
              , [205, 8, 1015]
              , [209, 9, 1101]
              , [210, 9, 1201]
              , [211, 9, 1311]
              , [212, 10, 1401]
              , [213, 10, 1514]
              , [213, 10, 1608]

          ],

          221: [
              [0, 0, 0]
              , [2, 0, 101]
              , [28, -3, 200]
              , [89, -17, 301]
              , [128, -28, 400]
              , [146, -28, 500]
              , [163, -29, 601]
              , [192, -36, 700]
              , [202, -37, 801]
              , [205, -39, 904]
              , [212, -41, 1001]
              , [213, -41, 1109]
              , [215, -42, 1210]
              , [219, -43, 1301]
              , [220, -43, 1410]
              , [221, -44, 1507]
          ],

          222: [
              [0, 0, 0]
              , [2, 0, 103]
              , [10, -1, 201]
              , [41, -5, 305]
              , [123, -15, 400]
              , [162, -19, 500]
              , [184, -23, 600]
              , [197, -27, 701]
              , [203, -28, 801]
              , [207, -29, 901]
              , [211, -29, 1000]
              , [216, -29, 1101]
              , [219, -28, 1201]
              , [221, -28, 1307]
              , [222, -27, 1401]
              , [222, -27, 1512]
              , [222, -27, 1615]

          ],

          226: [
              [0, 0, 0]
              , [10, -4, 100]
              , [51, -10, 201]
              , [108, -14, 301]
              , [130, -20, 401]
              , [149, -27, 500]
              , [166, -31, 601]
              , [182, -33, 703]
              , [193, -33, 801]
              , [202, -31, 904]
              , [207, -30, 1001]
              , [212, -28, 1100]
              , [214, -28, 1217]
              , [216, -28, 1301]
              , [218, -28, 1400]
              , [220, -28, 1501]
              , [222, -28, 1603]
              , [224, -28, 1700]
              , [226, -28, 1804]
              , [226, -28, 1903]
              , [226, -28, 2004]

          ],
          }

modelTraceX = [51, 53, 61, 65, 68, 74, 80, 88, 90, 92, 96, 99, 103, 106,
               115, 126, 127, 132, 140, 134, 148, 153, 154, 163, 166,
               174, 178, 186, 188, 191, 189, 200, 203, 211, 213, 221,
               222, 226]

DEFAULT_LIST = ['<i id="', 'imageEl', 'getBoundingClientRect', 'retryCount', 'getAutoSlideDefaultHtml', 'fromCharCode', 'networkFreshBtnEl', 'pass', 'rem', 'div', '@@iterator', 'event', '912940UOsOTF', './_export', 'afterResizeWidth', 'babel-runtime/helpers/typeof', '/pr/v1.0.3/img/icon-default.png', 'bottom', '" class="shumei_captcha_footer_close_btn"></div>', './_is-array', 'slideWidth', 'errMsg', 'seq_select', '__key', 'loading', './smLangMessage', 'mousedown', 'shumei_captcha_footer_refresh_btn', 'values', 'shumei_captcha_slide_tips', 'intervalTimer', 'onselectstart', 'null', 'shumei_captcha_img_loaded_wrapper', 'keyboardData', 'babel-runtime/helpers/classCallCheck', 'SMSdk', 'addEventListener', 'FIREFOX', 'preventDefaultHandler', 'slide_hover', '" class="shumei_captcha_slide_process"></div>', 'web', 'innerWidth', 'closePanelEvent', 'sm_', 'onError', 'fail', 'apply', '_Selenium_IDE_Recorder', 'answer_', 'fpMousemoveHandler', ', </font>', 'Symbol', '_successCallback', 'isIe678', 'smGetIdString', '© 2019 Denis Pushkarev (zloirock.ru)', 'Null', 'sliderPlaceholder', '42px', '__esModule', 'shumei_captcha_wrapper', 'getElementViewTop', 'scrollTop', './_cof', '" class="shumei_captcha_slide_btn"></div>', 'getInsensitiveDefaultHtml', ' Iterator', '7790460HPhbOe', 'inputEls', 'concat', '<img id="', 'fixProductSuccessStatus', ':&nbsp;&nbsp;', 'SDKVER', 'onload', 'selenium', 'shumei_captcha_popup_wrapper', '</span>', 'deviceId', 'insensitive_hover', '__nightmare', '_readyCallback', 'next', 'Cannot call a class as a function', 'Config load failure', './_iterators', '_pannel', '请依次点击', 'insensitive_disabled', './_library', '" class="shumei_captcha_img_loadding_wrapper">', './_uid', 'fpMouseClickHandler', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', 'pageY', 'resetPosition', '_bindNetworkEvent', 'extend', 'updateTplStatus', "', sizingMethod='crop')", './_classof', 'setRegisterData', 'call', 'head', 'aee9ca04', './_object-pie', 'substr', 'forEach', '485b2517', 'fromElement', 'slide_disabled', 'answer_content', '4ee2f32f', 'fixIE', 'mouseLeftClickData', 'push', 'navigator', '1.0.3', 'REJECT', '18IFwnSm', 'changePannelStatus', '/ca/v2/fverify', '" class="shumei_captcha shumei_captcha_wrapper">', 'rid', '_closeCallback', '../../modules/es6.symbol', 'constructor', 'mouseStartX', 'buildTpl', '../../modules/es7.symbol.async-iterator', 'mousemoveData', 'captchaTypeDomains', '%;left:', 'keyboardDataTimer', 'shumei_captcha_insensitive_tips', '\x00\x00\x00\x00\x00\x00\x00\x00', 'removeChild', 'touchmove', 'fVerifyUrl', 'beforeResizeWidth', 'isInitialized', '网络请求异常', '参数不合法', 'shumei_captcha_img_loadding_wrapper', ' is not an object!', 'registerApiInvalid', 'outHandler', 'top', 'fixProduct', 'floatOutTimer', 'isArray', 'attachEvent', 'debug', 'getPrototypeOf', 'checkApi', '_buildErrorHtml', '__webdriver_unwrapped', 'mouseRightClickDataTimer', 'keyboadStatus', 'join', 'insensitiveHandler', 'toString', 'mode', 'select_fail', 'shumei_captcha_slide_tips_wrapper', 'trueUnit', 'replace', 'compatMode', 'javascript:', 'shumei_show', 'registerData', 'getOwnPropertySymbols', 'images', 'constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf', 'smStringify', './_global', './_iter-create', 'fpMouseRightClickY', 'log', 'filter', 'touches', 'store', 'SERVER_ERROR', 'console', 'tracer', 'logError', 'Params invalid', 'sendRequest', './_enum-bug-keys', ' is not iterable!', 'contentWindow', "<i class='shumei_success_right'></i><span>Succeeded</span>", '1.1.3', 'indexOf', 'getResult', 'lang', 'BackCompat', '/script', 'slide_fail', 'object', './_add-to-unscopables', 'clientHeight', '<div class="shumei_captcha_insensitive_content">', 'shumei_captcha_img_loaded_fg_wrapper', 'imageFreshBtnEl', 'PASS', 'shumei_hide', 'removeEvent', 'Network failure|Click to retry', 'boolean', 'getElementsByClassName', 'hide', 'onerror', 'slideTipsTextEl', 'href', 'css', 'exports', 'slice', 'float', 'zh-cn', 'insensitiveMode', 'SMCaptcha', 'Array', '_captcha', '/ca/v1/conf', '" class="shumei_captcha_loaded_img_bg" />', 'captchaTypeUrl', 'load', '/pr/v1.0.3/img/icon-cry.png', '45658aGrazt', 'startHandler', 'location', 'clearClassStatus', 'UTF-8', '弹出层式验证码初始化失败', 'appendTo', 'min', '<input class="shumei_captcha_input_rid" type="hidden" name="rid" value="', 'getRootDom', '/pr/v1.0.3/img/icon-refresh.png', '" class="shumei_captcha_slide_tips_wrapper">', './_a-function', 'open', 'returnValue', 'width', 'data', 'popup', 'web_mobile', 'getMainDom', './core.get-iterator-method', 'http', 'keyboard', '52px', 'blockWidth', '/pr/v1.0.3/img/icon-move@2x.png', 'detail', 'clientWidth', 'saveEventList', 'Undefined', 'SVGPathSegList,SVGPointList,SVGStringList,SVGTransformList,SourceBufferList,StyleSheetList,TextTrackCueList,', 'Please click in order', './_has', 'core-js/library/fn/object/define-property', '0px', 'substring', 'Network failure', 'function', 'touchend', './_dom-create', 'fVerifyUrlV2', '2340954GZWdIa', 'className', 'getSelectPopupHtml', 'shumei_captcha_img_refresh_btn', 'setAttribute', 'advance', '../pkg/smImagesConf', 'value', 'shumei_', 'readyState', 'trueHeight', 'resetSuccessCallback', './_redefine', '__driver_unwrapped', 'shumei_captcha_img_load_error_wrapper', 'offsetParent', '8lHaYSf', 'userAgent', 'REVIEW', '" class="shumei_captcha_img_loaded_wrapper shumei_hide">', 'onClose', '../../modules/es6.string.iterator', 'imageLoadingEl', '        ', '_config', '/pr/v1.0.3/img/icon-success.png', 'footFreshBtnEl', 'setDomStyle', './_to-primitive', '_data', 'documentElement', 'splice', '" class="shumei_captcha_insensitive_tips">', 'Symbol is not a constructor!', '图片加载中...', 'showCaptcha', './_property-desc', 'getDeviceId', '_errorCallback', 'VERSION', 'network', '_each', '../modules/core.get-iterator', 'fixSize', 'shumei_captcha_img_loaded_bg_wrapper', 'fpMousemoveX', 'mouseRightClick', 'maskEl', 'onresize', '&nbsp;', 'message', '../pkg/smUtils', 'global', '" class="shumei_captcha_fail_refresh_btn"></i>', './_meta', 'isWidthInvalid', './_shared', 'reset', 'mouseEndX', 'CSS资源加载失败', 'getConsoleBywindowSize', 'slide', '%;" data-index="', 'getMouseAction', 'disabled', '/pr/v1.0.3/img/icon-move.png', ' is not a function!', 'cellectFullPageData', 'slideBtnEl', 'order', 'entries', 'shumei_captcha_footer_close_btn', 'saveMouseData', 'insensitive_fail', 'chrome', "url('./img/pixel.gif')", 'trueWidth', '../pkg/smCaptcha', 'return', '" class="shumei_captcha shumei_captcha_mask shumei_hide"></div>', '../core-js/symbol', '<div class="shumei_captcha_answer" style="top:', 'setResult', '2575232a', './_shared-key', './_to-iobject', 'mousemove', '/pr/v1.0.3/img/icon-popup-refresh@2x.png', 'http://', 'external', 'onSuccess', 'fixConfig', 'name', 'symbols', 'floor', 'toLocaleLowerCase', '/ca/v1/fverify', 'enumerable', 'saveFullPageData', 'updateAnswerHtml', 'no-network', 'success', 'sdkver', '../pkg/smObject', '" class="shumei_captcha_img_loaded_bg_wrapper">', 'riskLevel', './_object-keys-internal', '../../modules/_wks-ext', 'getElementsByTagName', 'customData', './_is-object', "<i class='shumei_success_wrong'></i><span>Failed</span>", 'code', 'imageLoadedBgEl', 'stringify', '[object Window]', './_descriptors', 'Arguments', 'getSlideDefaultHtml', 'String', 'currentStyle', 'changeImageStatus', '" class="shumei_captcha_slide_tips">', 'undefined', 'sort', 'captcha', 'core-js/library/fn/symbol/iterator', '" class="shumei_captcha shumei_captcha_popup_wrapper shumei_hide">', '/pr/v1.0.3/img/bg-default@2x.png', 'shumei_success_right', 'random', 'apiConf', '请按成语顺序点击', '</a>', 'initEvent', 'captcha.fengkongcloud.cn', 'shumei_captcha_img_wrapper', 'width:参数不合法', 'createElement', 'bindForm', './_iter-step', './_wks-define', 'isPc', '网络不给力|点击重试', 'get', 'getDefaultHtml', 'innerHeight', 'core-js/library/fn/get-iterator', "<i class='shumei_success_wrong'></i><span>验证失败,请重新验证</span>", './_core', 'normalizePath', 'base64Encode', 'panelEl', 'protocol', './_fails', 'CSSRuleList,CSSStyleDeclaration,CSSValueList,ClientRectList,DOMRectList,DOMStringList,', '当前网络不佳, 请刷新重试', '">\n                            <div class="answer_content" data-index="', '" class="shumei_captcha_network_fail_wrapper">', 'keyup', 'loadImages', 'getEncryptContent', 'shumei_captcha_network_fail_wrapper', '" class="shumei_captcha_loaded_img_fg" />', 'fpMouseLeftClickY', '33NWLNSI', 'toUpperCase', 'DataTimer', 'setImgUrl', 'shumei_captcha_slide_btn', 'insensitive', 'defineProperties', 'pageYOffset', 'meta', 'string', '" class="shumei_captcha_img_refresh_btn"></div>', 'rootDom', 'fpKeyboardHandler', 'captchaType', 'domains', 'Image load failure', 'resetForm', '_phantom', 'document.F=Object', '__core-js_shared__', '/pr/v1.0.3/img/bg-loading.png', '/pr/v1.0.3/img/icon-disabled.png', 'shumei_captcha_insensitive_wrapper', '/pr/v1.0.3/img/icon-fail.png', 'selectPosData', 'fpMouseRightClickX', 'src', './_object-create', 'slideEl', './_wks-ext', 'JS-SDK资源加载失败', 'click', 'keys', 'removeClass', 'valueOf', 'moveHandler', 'asyncIterator', 'scrollLeft', 'removeEventListener', 'match', './smEncrypt', 'floatOutHandler', '点击完成验证', 'fgEl', 'common', 'getFullPageData', './_to-integer', 'virtual', 'Math', 'webdriver', 'symbol', 'getAutoSlidePopupHtml', '../../modules/web.dom.iterable', 'shumei_captcha_input_rid', './es6.array.iterator', 'mouseLeftClick', '[null]', 'isNumber', 'wks', 'isRegisterInvalid', 'imagesLoaded', 'closeBtnEl', 'split', 'slideProcessEl', 'outerHeight', 'pure', 'fpMousemoveY', '/pr/v1.0.3/img/icon-success@2x.png', 'isString', './smLoad', 'mouseRightClickData', 'ff19d8d3', 'getAttribute', 'bindEvent', 'dec417a4', './_defined', 'shumei_captcha_loaded_img_bg', 'getJSONP', './_object-gopn', 'version', 'removeElement', 'mouseMoveX', '013f32d6', '__selenium_evaluate', './_object-dp', 'rel', 'registCaptcha', 'preventExtensions', '/ca/v1/register', '[object Array]', '图片资源加载失败', 'product', './_html', 'style', 'charCodeAt', 'isBoolean', '" class="shumei_captcha_img_loaded_fg_wrapper">', 'sshummei', 'networkFailEl', '__fxdriver_unwrapped', '</div>\n                        </div>', 'insensitiveTipsTextEl', 'selectData', '../../modules/es7.symbol.observable', 'changeRefreshBtnStatus', 'KEY', 'getRegisterData', './_object-gopd', 'mousemoveDataTimer', './smUtils', './_set-to-string-tag', '3754070VXNmZE', 'image', 'select', 'getPopupHtml', '</div>', 'absolute', '2.6.10', 'img', 'search', './_iter-define', 'closeHandler', 'versions', 'htmlNetwork', 'addClass', 'getElementByClassName', 'checkConsoleIsOpenHandler', './_wks', 'loadCss', 'fpMouseLeftClickX', '../../modules/es6.object.to-string', '/pr/v1.0.3/img/bg-loading@2x.png', 'setFirstRootDom', 'isObject', 'clearEvent', 'clientX', '__fxdriver_evaluate', 'DES', 'length', 'spatial_select', 'enableCaptcha', 'script', 'embed', 'toStringTag', 'mouseup', 'slide_success', 'babel-runtime/helpers/defineProperty', '/pr/v1.0.3/img/icon-close.png', 'innerHTML', '__userConf', 'return this', 'hasOwnProperty', '/pr/v1.0.3/img/bg-default.png', 'Object', './smStringify', 'Network failure, Try again', 'smGetElByClassName', 'parentNode', 'getInsensitiveCaTypeApi', './img/pixel.gif', '" class="shumei_captcha_img_wrapper">', 'getElementByTagName', 'background-position', 'shumei_captcha_mask', 'getOs', 'outerWidth', 'shumei_captcha_fail_refresh_btn', 'init', 'fixSuccessSize', '../pkg/smLoad', 'insensitiveProduct', 'icon_select', 'DEFAULT', 'checkResult', 'channel', 'status', './_object-dps', 'getSelectDefaultHtml', 'maxTouchPoints', 'mouseMoveY', '/pr/v1.0.3/img/bg-network.png', './_hide', 'target', 'shumei_captcha_slide_process', 'verify', 'shumei_captcha_loaded_img_fg', 'normalizeQuery', 'defineProperty', 'smDebounce', 'charset', 'startRequestTime', 'getIterator', 'ceil', 'onreadystatechange', 'Symbol.', 'initDom', '/pr/v1.0.3/img/bg-network@2x.png', 'pageX', 'initFreshEvent', '147', './_object-gpo', 'JSON', '_formDom', '" class="shumei_captcha_img_load_error_wrapper shumei_hide">', 'create', '" class="shumei_captcha_footer_refresh_btn"></div>', 'preventDefault', 'loadScript', 'floatOverHandler', '<div id="', '<span class="shumei_captcha_network_timeout">', 'prototype', 'iframe', 'endTime', 'auto', 'refreshHandler', 'mouseover', 'firstRootDomWidth', 'MediaList,MimeTypeArray,NamedNodeMap,NodeList,PaintRequestList,Plugin,PluginArray,SVGLengthList,SVGNumberList,', 'shumei_captcha_', 'op-symbols', 'registerUrl', 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx', '重置失败', 'propertyIsEnumerable', 'toLowerCase', 'c179010f', 'error', 'onReady', '/pr/v1.0.3/img/icon-cry@2x.png', './smObject', 'callee', 'appId', 'iterator', 'number', 'imageLoadedBgWrapperEl', '34314577opHAFY', 'ostype', '__webdriver_script_func', 'insensitiveEl', 'async', 'button', 'overHandler', 'DOMTokenList,DataTransferItemList,FileList,HTMLAllCollection,HTMLCollection,HTMLFormElement,HTMLSelectElement,', 'body', "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='", './_object-keys', 'getElementById', './_an-object', 'callPhantom', 'bind', 'getIteratorMethod', 'auto_slide', 'organization', '<div class="shumei_catpcha_footer_wrapper">', '9982035CVcgov', 'getSlidePopupHtml', '禁用验证码失败', '__webdriver_script_fn', 'touchstart', 'uuid', '100%', 'complete', 'ontouchstart', 'excuteCallback', 'insensitiveHandlerCallback', 'startTime', 'driver', '_selenium', 'input', 'imageLoadedFgEl', 'mouse', 'floatImagePosition', 'findChild', 'getUUID', 'data-index', '5NaoFez', '<span>', '/pr/v1.0.3/img/icon-refresh@2x.png', '<div class="shumei_captcha">', 'display', ':&nbsp;&nbsp; <img src="', 'detachEvent', './_ie8-dom-define', 'shumei_captcha_slide_wrapper', '" class="shumei_captcha_slide_wrapper">', 'hasInstance,isConcatSpreadable,iterator,match,replace,search,species,split,toPrimitive,toStringTag,unscopables', 'getTime', '../pkg/smConfig', 'imageLoadErrorEl', 'normalizeDomain', 'base64Decode', 'maskBindClose', '__webdriver_evaluate', 'shumei_captcha_form_result shumei_hide', 'charAt', 'rversion', 'captchaEl', 'appendTo参数异常', 'host', 'Css load failure', '/pr/v1.0.3/img/icon-fail@2x.png', 'default', './_iobject', 'maxRetryCount', '__selenium_unwrapped', 'Symbol(', 'offsetTop', 'smGetElById', 'show', 'Accessors not supported!', '../../modules/es6.object.define-property', 'selectPlaceholder', 'shumei_captcha_form_result', 'getMousePos', 'initOnceEvent', 'babel-runtime/core-js/get-iterator', 'Firebug', 'loadImage', 'reload', './_object-gops', 'https://', 'IE_PROTO', 'makeURL', 'tipsMessage', 'document', '../core-js/object/define-property', 'mouseData', 'mouseStartY', '/pr/v1.0.3/img/icon-close@2x.png', 'appendChild', 'insensitive_default', 'endHandler', 'mouseout', 'https', "Cannot find module '", 'selectHandler', 'hover', 'done', 'act.os', './_to-object', '/pr/v1.0.3/img/icon-default@2x.png', 'getOwnPropertyNames', 'runBotDetection']


def get_init_array():
    res = requests.get("http://127.0.0.1:4190/get_list")
    return res.json()["data"]


def zeroPad(data):
    """
    ZeroPadding
    """
    block_size = 8
    while len(data) % block_size:
        data += b"\0"
    return data


def desEncrypt(data, key):
    """des加密"""
    des_obj = pyDes.des(key.encode(), mode=pyDes.ECB)
    content = zeroPad(str(data).replace(" ", "").encode())
    return base64.b64encode(des_obj.encrypt(content)).decode(
        "utf-8")


def desDecrypt(data, key):
    """des解密"""
    return pyDes.des(key.encode(), mode=pyDes.ECB).decrypt(
        base64.b64decode(data)).decode("utf-8")



def getNearX(distX):
    # length = len(modelTraceX)
    nearX = 90
    # for i in range(length):
    #
    # 	if i <= length - 2 and modelTraceX[i] <= distX and distX < \
    # 		modelTraceX[i + 1]:
    # 		nearX = modelTraceX[i]
    # 		break
    # 	if i >= length - 1:
    # 		nearX = modelTraceX[-1]
    # 		break
    #
    # 	if distX <= modelTraceX[0]:
    # 		nearX = modelTraceX[0]
    # 		break

    return nearX


def creatTrace(distX):
    # 获取离其最近的distX的距离

    distX = round(distX * 0.516)

    distX = round(distX)

    nearX = getNearX(distX)

    # 获取标准轨迹
    trace = traces[nearX]
    # print('标准的长度{}，测出的长度{}'.format(nearX, distX))

    # 计算比例
    rate = distX / nearX

    # 根据比例求取制造轨迹
    # trace = [[0,0,0],[0,0,100],[8.421051025390625,-2.10528564453125,200],[21.052627563476562,-7.368438720703125,301],[42.105262756347656,-10.526336669921875,401],[62.105262756347656,-10.526336669921875,501],[93.68421936035156,-8.42108154296875,601],[106.3157958984375,-8.42108154296875,701],[135.7894744873047,-9.47369384765625,801],[151.57894897460938,-9.47369384765625,901],[160,-9.47369384765625,1001],[169.47369384765625,-9.47369384765625,1101],[184.2105255126953,-13.684234619140625,1200],[190.5263214111328,-15.78948974609375,1302],[196.8421173095703,-16.842132568359375,1402],[200.00001525878906,-18.9473876953125,1500],[202.1052703857422,-18.9473876953125,1609],[202.1052703857422,-18.9473876953125,1702],[202.1052703857422,-18.9473876953125,1810],[202.1052703857422,-18.9473876953125,1904],[202.1052703857422,-18.9473876953125,2012]]

    newTrace = [[int(xyt[0] * rate), xyt[1], xyt[2]] for xyt in trace]

    # print(newTrace)
    return distX, newTrace


def bgImDecode(bg_content):
    bg_img = cv2.imdecode(np.frombuffer(bg_content, np.uint8),
                          cv2.IMREAD_COLOR)  # 如果是PIL.images就换读取方式
    bg_edge = cv2.Canny(bg_img, 100, 200)
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    return bg_pic


def tpImgDecode(ct_content):
    tp_img = cv2.imdecode(np.frombuffer(ct_content, np.uint8),
                          cv2.IMREAD_COLOR)

    tp_edge = cv2.Canny(tp_img, 100, 200)

    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
    return tp_pic


def match(bg_pic, tp_pic):
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    return res


def get_xy(bg_content: bytes, ct_content: bytes):
    bg_pic = bgImDecode(bg_content)
    tp_pic = tpImgDecode(ct_content)

    res = match(bg_pic, tp_pic)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # th, tw = tp_pic.shape[:2]
    # print('缺口所在的位置，x是--->{},y是--->{}'.format(max_loc[:2][0],max_loc[:2][1]))

    return max_loc[:2]


def GetData(bg_content, ct_content):
    distX, distY = get_xy(bg_content, ct_content)
    distX, newTrace = creatTrace(distX)
    return newTrace[-1][0], newTrace


def getTrace(bgContent, fgConten):
    startTime = round(time.time() * 1000)
    mouseEndX, mouseData = GetData(bgContent, fgConten)
    endTime = startTime + 7 + mouseData[-1][-1]
    print(mouseEndX, mouseData[-1][0], startTime, endTime)
    trace = {
        "selectData": [

        ],
        "trueWidth": 310.40000000000003,
        "trueHeight": 155.20000000000002,
        "blockWidth": 46.5,
        "endTime": endTime,
        "mouseEndX": mouseEndX,
        "mouseData": mouseData,
        "startTime": startTime
    }
    return trace

# PC
def get_params(js_list, rid, trace, now_time):
    print("mouseEndX: ", trace["mouseEndX"])
    parmas = {
        "dl": desEncrypt(str(float(trace["mouseEndX"]/300)), js_list[int(0x325)-450]),   # X初始坐标
        "nm": desEncrypt(trace["mouseData"], js_list[int(0x234)-450]),  # 轨迹
        "dy": desEncrypt(str(trace["endTime"] - trace["startTime"]), "aee9ca04"),  # 动态时间
        "lx": desEncrypt("300", js_list[int(0x3c1)-450]),
        "xy": desEncrypt("150", js_list[int(0x459)-450]),
        "vk": desEncrypt("1", "2323fc45"),
        "ux": desEncrypt("0", "8d1339ba"),
        "xp": desEncrypt("-1", js_list[int(0x3be)-450]),
        "aw": desEncrypt("default", js_list[int(0x3c9)-450]),
        "gi": desEncrypt("DEFAULT", "bc1b5ed3"),
        "oe": desEncrypt("zh-cn", "59bca469"),
        "act.os": "web_pc",
        "organization": "RlokQwRlVjUrTUlkIqOg",
        "sdkver": "1.1.3",
        "rversion": "1.0.3",
        "callback": "sm_" + str(now_time),
        "protocol": "147",
        "ostype": "web",
        "rid": rid
    }
    pprint(parmas)
    return parmas


def register():
    now_time = int(time.time())
    url = "https://captcha.fengkongcloud.cn/ca/v1/register?organization=RlokQwRlVjUrTUlkIqOg&appId=default&channel=DEFAULT" \
          f"&lang=zh-cn&model=slide&rversion=1.0.3&sdkver=1.1.3&data=%7B%7D&callback=sm_{now_time}"
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'script',
        'Referer': 'https://www.ishumei.com/trial/captcha.html',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    res = requests.get(url, headers)
    print(res.text)
    return res.text.replace(str("sm_" + str(now_time) + "("), "")[:-1], now_time


def fverify(params):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'script',
        'Referer': 'https://www.ishumei.com/trial/captcha.html',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    response = requests.get('https://captcha.fengkongcloud.cn/ca/v2/fverify', headers=headers, params=params)
    print(response.text)
    return response.text


def downPhoto(bgUrl, fgUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    bgUrl = 'https://castatic.fengkongcloud.com' + bgUrl
    fgUrl = 'https://castatic.fengkongcloud.com' + fgUrl

    bgRespone = requests.get(bgUrl, headers=headers)
    bgContent = bgRespone.content
    fgResponse = requests.get(fgUrl, headers=headers)
    fgConten = fgResponse.content
    return bgContent, fgConten


def main():
    register_result, now_time = register()
    print(register_result)
    register_result = json.loads(register_result)
    bgUrl = register_result["detail"]["bg"]
    fgUrl = register_result["detail"]["fg"]
    k = register_result["detail"]["k"]
    rid = register_result["detail"]["rid"]
    bgContent, fgContent = downPhoto(bgUrl, fgUrl)
    trace = getTrace(bgContent, fgContent)
    params = get_params(DEFAULT_LIST, rid, trace, now_time)
    result = fverify(params)
    if "PASS" in result:
        pass


if __name__ == '__main__':
    # [[0,0,0],[10,0,100],[110,-2,201],[133,-2,301],[136,-8,402],[137,-10,500],[132,-11,601],[131,-11,707],[131,-11,814],[131,-11,905]]
    # slide = desDecrypt('2Llzh5Trqkb4y8plE1Qoc3j06Fhh1AYeW4GWECualefu+NsCncV5ej+JY9YMAI2FZY5xuVPFPwPhxIW0rFP22pDl47NhhphYX7NmQOLtSPbYYoxJkhtMqQ4Djk/rG5m0RkpZzjqD1Spvuy1U4+x7hfX7K0r0js5/kjLMoqIVC7UKAyexvJG2Rw==', DEFAULT_LIST[int(0x234)-450])
    # print(slide)
    main()



