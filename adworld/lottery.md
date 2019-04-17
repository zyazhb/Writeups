git文件泄露

审计

其中 $numbers 来自用户json输入 {"action":"buy","numbers":"1122334"}，没有检查数据类型。 $win_numbers 是随机生成的数字字符串。
使用 PHP 弱类型松散比较，以"1"为例，和TRUE,1,"1"相等。 由于 json 支持布尔型数据，因此可以抓包改包，构造数据：

{"action":"buy","numbers":[true,true,true,true,true,true,true]}
当每一位中奖号码都不是0时即可中最高奖，攒钱买flag。
