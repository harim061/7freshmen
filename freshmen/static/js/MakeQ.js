//번호 인덱싱
const indexingQnum = () => {
  const numlength = $(".question_num").length;
  const numArr = $(".question_num").get();
  for (var i = 0; i < numlength; i++) {
    numArr[i].innerHTML = i + 1;
  }
};
//폼 유효성 검사
const form_check = (form) => {
  var form_check;
  $(form)
    .find("input[type=text]")
    .each(function () {
      if ($(this).val().trim() == "") {
        $(this).focus();
        form_check = false;
        return false;
      } else {
        form_check = true;
      }
    });
  return Boolean(form_check);
};
//폼 제출
const submit_form = () => {
  if (!form_check(question)) {
    return;
  }
  $("#submitQ").trigger("click");
};
//질문 div 추가
const add_question = () => {
  var Q_num = $(".question_warp").length;
  const temp = `<section class="question_warp">
    <div class="question_list">
      <div class="question_num"></div>
      <input
        name="question[]"
        class="question_input"
        type="text"
        placeholder="문제를 써주세요 ex)내가 좋아하는 음식은?"
        onfocus="this.placeholder=''"
        onblur="this.placeholder='문제를 써주세요 ex)내가 좋아하는 음식은?'"
      />
      <button
        type="button"
        class="question_delete"
        onclick="delete_question(event)"
      >
        x
      </button>
    </div>
    <div class="answer_warp">
      <input
        name="op1[]"
        class="answer"
        id="answer_true"
        type="text"
        placeholder="정답 : ex) 떡볶이"
        onfocus="this.placeholder=''"
        onblur="this.placeholder='정답 : ex) 떡볶이'"
      />
      <div class="vs_circle">VS</div>
      <input
        name="op2[]"
        class="answer"
        id="answer_false"
        type="text"
        placeholder="오답 : ex) 치킨"
        onfocus="this.placeholder=''"
        onblur="this.placeholder='오답 : ex)치킨'"
      />
    </div>
    <p class="alert_text">
      정답은 왼쪽 칸에 오답은 오른쪽 칸에 적어주세요!
    </p>
  </section>`;
  
  if (!Qnum_check(Q_num)) {
    return;
  }
  $("#question").append($(temp));
  indexingQnum();
};
//div 5개 이상시 경고 메세지 출력
const Qnum_check = (index) => {
  if (index > 4) {
    $("#smaller_alert").text("문제는 최대 5개까지 가능해요!");
    return false;
  } else {
    $("#smaller_alert").text("");
    return true;
  }
};
//div question 삭제
const delete_question = (event) => {
  $("#smaller_alert").text("");
  var Q_num = $(".question_warp").length;
  if (Q_num === 1) {
    return;
  }
  var dv = event.currentTarget;
  $(dv).closest("section").remove();
  indexingQnum();
};