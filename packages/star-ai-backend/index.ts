import Express from 'express';
import Config from './config/dotfiles';

const app = Express(); // Initilizing an express app

app.get('/', (req, res) => {
    res.status(200).send('Hello, World');
});

app.listen(Config.httpServer.port, () => {
    console.log(`Server is running on http://${Config.httpServer.host}:${Config.httpServer.port}`);
});
