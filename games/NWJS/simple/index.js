nw.Window.open('./index.html', {}, (win) => {
    const win = nw.Window.get();
    const width = 288;
    const height = 224;
    win.setMaximumSize(width, height);
    win.setMinimumSize(width, height);
});

add_shortcut("Escape");

function add_shortcut(key_shortcut){
    const option = {
        key: key_shortcut,
	active () {
	    nw.App.quit();
	},
	failed (msg) {
	    console.log(msg);
	}
    };
    const shortcut = new nw.Shortcut(option);
    nw.App.registerGlobalHotKey(shortcut);
}
