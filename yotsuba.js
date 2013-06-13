function showAllKana() {
	if ($(".kana").is(":hidden")){
		$(".kana").show()
		$(".kana").parent().siblings(".individual-btn").text("Show Translation")
		$(".all-kana").text("Hide Kana with Kanji")
	}
	else {
		$(".kanji").parent().siblings().children(".kana").hide()
		$(".kana").parent().siblings(".individual-btn").text("Show Translation")
		$(".kanji").parent().siblings(".individual-btn").text("Show Kana")
		$(".all-kana").text("Show All Kana")
	}
}

function showAllTrans() {
	if ($(".trans").is(":hidden")){
		$(".trans").show()
		$(".all-trans").text("Hide All Translations")
	}
	else {
		$(".trans").hide()
		$(".all-trans").text("Show All Translations")
	}
}

function hideAll() {
	$(".kanji").parent().siblings().children(".kana").hide()
	$(".trans").hide()
}

$(document).ready(function() {
	$("td:nth-child(2):empty").siblings().children(".kana").show()
	$("td:nth-child(2):empty").siblings(".individual-btn").text("Show Translation")

	$(".individual-btn").click(function () {
		var kana = $(this).siblings().children(".kana")
		var trans = $(this).siblings().children(".trans")
		if (kana.is(":visible") && trans.is(":visible")){
			trans.hide()
			$(this).text("Show Translation")	
		}
		else if (kana.is(":visible")) {
			trans.show()
		}
		else if (kana.not(":visible")) {
			kana.show()
			$(this).text("Show Translation")	
		}
		if (kana.is(":visible") && trans.is(":visible")){
			$(this).text("Hide Translation")
		}
	})
})
