class reminder{
    constructor(content = ""){
        this._content = content;
    }
    get content() {
        return this._content;
    }
    set content(someVal){
        this._content = someVal;
    }
}

ne = new reminder()
ne.content = 1

console.log(ne.content)