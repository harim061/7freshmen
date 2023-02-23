function btnShareTw(text){
    const sendText = text;
    const pageUrl = 'news.v.daum.net/v/20220319120213003';
    window.open(`https://twitter.com/intent/tweet?text=${sendText}&url=${pageUrl}`);
}