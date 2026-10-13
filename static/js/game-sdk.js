// What every game gets: DjGame.canvas, DjGame.loggedIn, await DjGame.load(), DjGame.save(state).
// Settings come from data-* attributes on <canvas id="game"> in game/play.html.
// Wrapped in a block so names here can't clash with a game's own top-level variables.
{
    const canvas = document.getElementById('game');

    window.DjGame = {
        canvas,
        loggedIn: canvas.dataset.loggedIn === 'true',

        async load() {
            if (!this.loggedIn) return null;
            const res = await fetch(canvas.dataset.saveUrl);
            return res.ok ? (await res.json()).data : null;
        },

        async save(state) {
            if (!this.loggedIn) return false;
            const res = await fetch(canvas.dataset.saveUrl, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json', 'X-CSRFToken': canvas.dataset.csrfToken },
                body: JSON.stringify(state),
            });
            return res.ok;
        },
    };
}
