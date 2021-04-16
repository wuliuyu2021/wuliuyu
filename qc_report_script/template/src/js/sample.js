$(function() {
    if (document.getElementById("lct")){
    	var myChart = echarts.init(document.getElementById('lct'),'shine');
    	    var option = {
    	        title: {
    	        		text:"",
    	        		padding:5,
    	        		textStyle: {
        						fontSize: 15,
        						fontWeight: 'bolder',
        						color: '#333'    
    			},		 
    	        },
    	        tooltip: {
    	        	"formatter": function(param) {
           
            				return param.data.category;
        			}
    	        },
    	        //animationDurationUpdate: 1500,
    			//animationEasingUpdate: 'quinticInOut',
    			series : [
   				{
            		type: 'graph',
            		layout: 'none',
            		symbolSize: [100,50],
            		roam: false,
            		label: {
                		normal: {
                    	show: true,
						position:"inside",
                	}
            	},
            //edgeSymbol: ['circle', 'arrow'],
            //edgeSymbolSize: [4, 8],
          
            data: [{
                name: "原始数据",
                x:200,
                y: 50,
               	//"value": "22",
            	//"draggable": "true"
            	"category": "1、原始数据过滤<br>2、碱基质量分布<br>3、碱基含量分布<br>4、测序数据统计"

            }, {
                name: "数据质控",
                x:200,
                y: 75
            }, {
                name: "数据比对",
                x:200,
                y: 100,
				
            }, {
                name: "可变剪接",
                x:155,
                y: 90,
				//itemStyle:{color:"#1E90FF"}
            },{
				name:"变异位点、注释",
				x:155,
				y:110,
			},{
				name:"差异分析",
				x:200,
				y:125
			},{
				name:"融合基因",
				x:245,
				y:100,
			}],
            // links: [],
            links: [ {
                source: "原始数据",
                target: "数据质控",

            }, {
                source: "数据质控",
                target: "数据比对"
            }, {
                source: "数据比对",
                target: "差异分析"
            },{
				source:"数据比对",
				target:"可变剪接"
			},{
				source:"数据比对",
				target:"变异位点、注释",
			},{
				source:"数据比对",
				target:"融合基因"
			},],
			"symbol": "path://M19.300,3.300 L253.300,3.300 C262.136,3.300 269.300,10.463 269.300,19.300 L269.300,21.300 C269.300,30.137 262.136,37.300 253.300,37.300 L19.300,37.300 C10.463,37.300 3.300,30.137 3.300,21.300 L3.300,19.300 C3.300,10.463 10.463,3.300 19.300,3.300 Z",
			//"focusNodeAdjacency": true,
            lineStyle: {
                normal: {
                    opacity: 0.9,
                    width: 2,
                    curveness: 0
                }
            }
        }
    ]
	};
    	  	myChart.setOption(option);
  };

  
});