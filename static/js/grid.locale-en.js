!function(a){
	"use strict";
	"function"==typeof define&&define.amd?define(["jquery","../grid.base"],a):a(jQuery)
}
(
	function(a){a.jgrid=a.jgrid||{},
	a.jgrid.hasOwnProperty("regional")||(a.jgrid.regional=[]),
	a.jgrid.regional.en={
		defaults:{
			recordtext:"View {0} - {1} of {2}",
			emptyrecords:"No records to view",
			loadtext:"Loading...",
			savetext:"Saving...",
			pgtext:"Page {0} of {1}",
			pgfirst:"First Page",
			pglast:"Last Page",
			pgnext:"Next Page",
			pgprev:"Previous Page",
			pgrecs:"Records per Page",
			showhide:"显示/隐藏 表格",
			pagerCaption:"Grid::Page Settings",
			pageText:"Page:",
			recordPage:"Records per Page",
			nomorerecs:"No more records...",
			scrollPullup:"Pull up to load more...",
			scrollPulldown:"Pull down to refresh...",
			scrollRefresh:"Release to refresh..."
		},
		search:{
			caption: "搜索中...",
			Find: "查找",
			Reset: "重置",
			odata: [{ oper:'eq', text:'等于'},{ oper:'ne', text:'不等于'},{ oper:'lt', text:'小于'},{ oper:'le', text:'小于等于'},{ oper:'gt', text:'大于'},{ oper:'ge', text:'大于等于'},{ oper:'bw', text:'开始于'},{ oper:'bn', text:'不开始于'},{ oper:'in', text:'处于'},{ oper:'ni', text:'不处于'},{ oper:'ew', text:'结束于'},{ oper:'en', text:'不结束于'},{ oper:'cn', text:'包含'},{ oper:'nc', text:'不包含'}],
			groupOps: [  { op: "AND", text: "并且" }, { op: "OR",  text: "或者" } ],
			operandTitle:"Click to select search operation.",
			resetTitle:"Reset Search Value"},
		edit:{
			addCaption: "添加记录",
			editCaption: "编辑记录",
			bSubmit: "提交",
			bCancel: "取消",
			bClose: "关闭",
			saveData: "数据已更改！ 是否提交更改？",
			bYes : "是",
			bNo : "不",
			bExit : "取消",
			msg: {
				required:"此字段必需",   
				number:"请输入有效数字",   
				minValue:"输入值必须大于等于",   
				maxValue:"输入值必须小于等于",   
				email: "这不是有效的e-mail",
				integer: "请输入有效的整数值",
				date: "请输入有效的日期值",
				url: "不是合法的URL格式！ 必须以('http://' or 'https://')开始",
				nodefined : "不存在！",
				novalue : "无返回值！",
				customarray : "必须返回数组！",
				customfcheck : "请检查！"
			}
		},
		view:{
			caption:"View Record",
			bClose:"Close"
		},
		del:{
			caption:"提示：",
			msg:"你要删除这条记录吗?",
			bSubmit:"删除",bCancel:"取消"
		},
		nav:{
			edittext:"",
			edittitle:"Edit selected row",
			addtext:"",
			addtitle:"Add new row",
			deltext:"",
			deltitle:"Delete selected row",
			searchtext:"",
			searchtitle:"Find records",
			refreshtext:"",
			refreshtitle:"Reload Grid",
			alertcap:"警告：",
			alerttext:"请选择一条记录",
			viewtext:"",
			viewtitle:"View selected row",
			savetext:"",
			savetitle:"Save row",
			canceltext:"",
			canceltitle:"Cancel row editing",
			selectcaption:"Actions..."
		},
		col:{
			caption:"Select columns",
			bSubmit:"Ok",
			bCancel:"Cancel"
		},
		errors:{
			errcap:"Error",
			nourl:"No url is set",
			norecords:"No records to process",
			model:"Length of colNames <> colModel!"
		},
		formatter:{
			integer:{
				thousandsSeparator:",",
				defaultValue:"0"
			},
			number:{
				decimalSeparator:".",
				thousandsSeparator:",",
				decimalPlaces:2,
				defaultValue:"0.00"
			},
			currency:{
				decimalSeparator:".",
				thousandsSeparator:",",
				decimalPlaces:2,
				prefix:"",
				suffix:"",
				defaultValue:"0.00"
			},
			date:{
				dayNames:[
            		"日","一","二","三","四","五","六",
            		"星期日","星期一","星期二","星期三","星期四","星期五","星期六"
            	],
            	monthNames: [
            		"一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二",
            		"一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"
            	],
				AmPm:[
					"am",
					"pm",
					"AM",
					"PM"
				],
				S:function(a){
					return 11>a||a>13?["st","nd","rd","th"][Math.min((a-1)%10,3)]:"th"},
				srcformat:"Y-m-d",
				newformat:"n/j/Y",
				parseRe:/[#%\\\/:_;.,\t\s-]/,
				masks:{
					ISO8601Long:"Y-m-d H:i:s",
					ISO8601Short:"Y-m-d",
					ShortDate:"n/j/Y",
					LongDate:"l, F d, Y",
					FullDateTime:"l, F d, Y g:i:s A",
					MonthDay:"F d",
					ShortTime:"g:i A",
					LongTime:"g:i:s A",
					SortableDateTime:"Y-m-d\\TH:i:s",
					UniversalSortableDateTime:"Y-m-d H:i:sO",
					YearMonth:"F, Y"
				},
				reformatAfterEdit:!1,
				userLocalTime:!1
			},
			baseLinkUrl:"",
			showAction:"",
			target:"",
			checkbox:{disabled:!0},idName:"id"}
		}
	}
);
