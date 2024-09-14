import Express from 'express';
import Config from './config/dotfiles';

import bodyParser from 'body-parser';

// Routes
import TestRoute from './routes/test';

const app = Express(); // Initilizing an express app

app.use((req, res, next) => {
    console.log(`Request made to: ${req.path}`);
    res.on('finish', () => {
        console.log(`Response status: ${res.statusCode}`);
    });
    next();
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use((req, res, next) => {
	res.header('Access-Control-Allow-Origin', '*');
	res.header(
		'Access-Control-Allow-Headers',
		'Origin, X-Requested-With, Content-Type, Accept, Authorization'
	);

	if (req.method === 'OPTIONS') {
		res.header('Access-Control-Allow-Methods', 'GET PATCH DELETE POST PUT');
		return res.status(200).json({});
	}

	next();
});

app.use('/api/test', TestRoute);

app.listen(Config.httpServer.port, () => {
    console.log(`Server is running on http://${Config.httpServer.host}:${Config.httpServer.port}`);
});
