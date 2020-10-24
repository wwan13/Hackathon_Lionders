// $(document).ready(function() {
//     //datepicker 한국어로 사용하기 위한 언어설정
//     $.datepicker.setDefaults($.datepicker.regional['ko']);     

//     // Datepicker            
//     $(".datepicker").datepicker({
//         showButtonPanel: true,
//         dateFormat: "yy-mm-dd",
//         onClose : function ( selectedDate ) {
        
//             var eleId = $(this).attr("id");
//             var optionName = "";

//             if(eleId.indexOf("StartDate") > 0) {
//                 eleId = eleId.replace("StartDate", "EndDate");
//                 optionName = "minDate";
//             } else {
//                 eleId = eleId.replace("EndDate", "StartDate");
//                 optionName = "maxDate";
//             }

//             $("#"+eleId).datepicker( "option", optionName, selectedDate );        
//             $(".searchDate").find(".chkbox2").removeClass("on"); 
//         }
//     }); 

//     //시작일.
//     /*$('#searchStartDate').datepicker("option","onClose", function( selectedDate ) {    
//         // 시작일 datepicker가 닫힐때
//         // 종료일의 선택할수있는 최소 날짜(minDate)를 선택한 시작일로 지정
//         $("#searchEndDate").datepicker( "option", "minDate", selectedDate );
//         $(".searchDate").find(".chkbox2").removeClass("on");
//     });
//     */

//     //종료일.
//     /*$('#searchEndDate').datepicker("option","onClose", function( selectedDate ) {    
//         // 종료일 datepicker가 닫힐때
//         // 시작일의 선택할수있는 최대 날짜(maxDate)를 선택한 종료일로 지정 
//         $("#searchStartDate").datepicker( "option", "maxDate", selectedDate );
//         $(".searchDate").find(".chkbox2").removeClass("on");
//     });
//     */

//     $(".dateclick").dateclick();    // DateClick
//     $(".searchDate").schDate();        // searchDate
    
// });

// // Search Date
// jQuery.fn.schDate = function(){
//     var $obj = $(this);
//     var $chk = $obj.find("input[type=radio]");
//     $chk.click(function(){                
//         $('input:not(:checked)').parent(".chkbox2").removeClass("on");
//         $('input:checked').parent(".chkbox2").addClass("on");                    
//     });
// };

// // DateClick
// jQuery.fn.dateclick = function(){
//     var $obj = $(this);
//     $obj.click(function(){
//         $(this).parent().find("input").focus();
//     });
// }    


// function setSearchDate(start){

//     var num = start.substring(0,1);
//     var str = start.substring(1,2);

//     var today = new Date();

//     //var year = today.getFullYear();
//     //var month = today.getMonth() + 1;
//     //var day = today.getDate();
    
//     var endDate = $.datepicker.formatDate('yy-mm-dd', today);
//     $('#searchEndDate').val(endDate);
    
//     if(str == 'd'){
//         today.setDate(today.getDate() - num);
//     }else if (str == 'w'){
//         today.setDate(today.getDate() - (num*7));
//     }else if (str == 'm'){
//         today.setMonth(today.getMonth() - num);
//         today.setDate(today.getDate() + 1);
//     }

//     var startDate = $.datepicker.formatDate('yy-mm-dd', today);
//     $('#searchStartDate').val(startDate);
            
//     // 종료일은 시작일 이전 날짜 선택하지 못하도록 비활성화
//     $("#searchEndDate").datepicker( "option", "minDate", startDate );
    
//     // 시작일은 종료일 이후 날짜 선택하지 못하도록 비활성화
//     $("#searchStartDate").datepicker( "option", "maxDate", endDate );

// }

function setSearchDate(start){
    let setPeriod = '';
    switch(start){
        case '1w':
            setPeriod = 7;
            break;
        case '1m':
            setPeriod = 31;
            break;
        case '3m':
            setPeriod = 92;
            break;
        case '6m':
            setPeriod = 183;
            break;
        default:
            setPeriod = 0;
            break;
    }
    document.getElementById("period").value = setPeriod;
}

function estimating(point){
    let setEstimate = 0;
    switch(point){
        case '1.0':
            setEstimate = 1.0;
            break;
        case '2.0':
            setEstimate = 2.0;
            break;
        case '3.0':
            setEstimate = 3.0;
            break;
        case '4.0':
            setEstimate = 4.0;
            break;
        case '5.0':
            setEstimate = 5.0;
            break;
        default:
            setEstimate = 0.0;
            break;
    }
    document.getElementById("estimate").value = setEstimate;
}