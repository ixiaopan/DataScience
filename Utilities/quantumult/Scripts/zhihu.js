// 网页版PC去登录弹框、底部跳转APP提示
let body=$response.body

identifier = '</script></head>'
insert_pos = body.indexOf(identifier)

if (insert_pos > -1) {
  work = 'setTimeout(function(){const linksinRich=document.querySelectorAll(".RichContent-inner a");(linksinRich || []).forEach(e => {if (e.href.indexOf("link.zhihu.com") > -1) {const query = {};const queryStr = e.href.split("?")[1];((queryStr && queryStr.split("&")) || []).forEach(s => {const sq = s.split("=");if (sq && sq.length) {query[sq[0]] = sq[1];}});e.href = decodeURIComponent(query["target"]);}}); const recomZhuanlan = document.querySelectorAll(".MobilePostItem");(recomZhuanlan || []).forEach(e => e.addEventListener("touchend", function (e) { e.preventDefault();location.href=e.currentTarget.href;})); const openInAppButton = document.querySelector(".OpenInAppButton"); if (openInAppButton) { openInAppButton.style.display = "none"; } const closeBtn = document.querySelector(".Modal-closeButton"); if (closeBtn) { closeBtn.click() }; const btns = document.querySelectorAll(".ModalExp-modalShow .ModalWrap-itemBtn"); if (btns && btns.length && btns[1]) { btns[1].click(); }}, 2500)';
  body = body.slice(0, insert_pos) + work + body.slice(insert_pos)
}

$done({ body: body })
