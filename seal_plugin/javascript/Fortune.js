// ==UserScript==
// @name         山山的今日运势
// @author       MP
// @version      1.1.0
// @description  示例：抽取牌堆&调用自定义文案
// @timestamp    1722421192
// @license      Apache-2
// @homepageURL  暂无
// ==/UserScript==

let ext = seal.ext.find('运势')
if (!ext) {
  ext = seal.ext.new('运势', 'Mp', '1.1.0');
  seal.ext.register(ext);
}

function getBaseLog(x, y) {
  return Math.log(y) / Math.log(x);
}

function daytime()
{
  var today = new Date();
  var year = today.getFullYear(); // 获取当前年份，例如 2024
  var month = today.getMonth() + 1; // 获取当前月份，从 1 开始计数
  var day = today.getDate(); // 获取当前日期
  var numericDate = year * 10000 + month * 100 + day;// 将年、月、日组合成一个数字形式的日期
  return numericDate;
}

function gettime()
{
  var today = new Date();
  return today.getTime();
}

// 简单函数：将字符串映射为数字
function mapStringToNumber(input) {
  var num = 0;
  for (var i = 0; i < input.length; i++) {
      num += input.charCodeAt(i); // 将每个字符的 ASCII 码相加
  }
  return num;
}
//重构了random函数
Math.seededRandom = function(max, min, seed) {
  max = max || 100;
  min = min || 0;

  seed = (seed * 9301 + 49297) % 233280;
  var rnd = seed / 233280.0;

  return Math.ceil( min + rnd * (max - min) );   // Math.ceil实现取整功能，可以根据需要取消取整
};

const cmd = seal.ext.newCmdItemInfo();
cmd.name = 'test';
cmd.help = '抽取一个调查员';
cmd.solve = (ctx, msg, cmdArgs) => {
  let dayseed = mapStringToNumber(ctx.player.userId)  //读取用户id，转换为数字形式再作为随机的seed
  dayseed += daytime();
  let dayF1 = Math.seededRandom(100,0,dayseed);//财运
  let dayF2 = Math.seededRandom(100,0,dayseed*2);//桃花运
  let dayF3 = Math.seededRandom(100,0,dayseed*3);//事业运
  let nowseed = mapStringToNumber(ctx.player.name);
  nowseed += gettime() ;
  let nowF =Math.seededRandom(20,-20,nowseed);



  //提高大家的运气
dayF1 = Math.ceil(getBaseLog(2,(dayF1/33.3)+1)*49.9725);
dayF2 = Math.ceil(getBaseLog(2,(dayF2/33.3)+1)*49.9725);
dayF3 = Math.ceil(getBaseLog(2,(dayF3/33.3)+1)*49.9725);


nowF += (dayF1+dayF2+dayF3)/3;
if(nowF > 100)
{
  nowF = 100;
}
else if (nowF < 1)
{
  nowF = 1;
}

nowF = (Math.ceil(nowF));


  let dianping = "";
  if(dayF1+dayF2+dayF3>=200)
  {
    dianping += "大吉";
  }
  else if(dayF1+dayF2+dayF3>=100)
  {
    dianping += "中吉";
  }
  else
  {
    dianping += "凶";
  }
  if(dayF1>= 80)
  {
    dianping += "，财运";
  }
  if(dayF2>= 80)
  {
    dianping += "，桃花运";
  }
  if(dayF3>= 80)
  {
    dianping += "，官运";
  }

  //seal.replyToSender(ctx, msg,ctx.player.userId);

  seal.replyToSender(ctx, msg, "诗岸为您祈祷今日份的美梦~您今日的运势为...\n今日财运："+dayF1+"\n今日桃花运："+dayF2+"\n今日事业运："+dayF3+"\n现在运势："+nowF+"\n点评："+dianping);
  return seal.ext.newCmdExecuteResult(true);
};
ext.cmdMap['今日运势'] = cmd;