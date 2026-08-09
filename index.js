const express = require('express');
const app = express();

app.use(express.json());

app.post('/tasks', (req, res) => {
    const newTask = {
        id: tasks.length + 1,
        title: req.body.title,
        done: false
    };
    tasks.push(newTask);
    // request succeeded, new resource was created
    res.status(201).json(newTask);
});

let tasks = [
    { id: 1, title: 'Learn express', done: false },
    { id: 2, title: 'Write first test', done: false }
];

app.get('/', (req, res) => {
    res.send('server is running')
    // 200 : OK (the request succeeded)
    // no need to write status explicitly since it is the default for :
    // GET, HEAD, PUT-POST, TRACE
    res.status(200).json(task);
});

app.get('/tasks', (req, res) => {
    res.json(tasks);
});

app.get('/tasks/:id', (req, res) => {
    const taskId = parseInt(req.params.id);
    const task = tasks.find(t => t.id === taskId);
    if (!task) {
        return res.status(404).json({ error: 'Task not found' });
    }

    res.json(task);
});

app.put('/tasks/:id', (req, res) => {
    const taskId = parseInt(req.params.id);
    const task = tasks.find(task => task.id === taskId);

    if (!task) {
        return res.status(404).json({ error: 'Task not found' });
    }

    // if one field isn't sent then don't try to update that field
    if (req.body.title !== undefined) {
        task.title = req.body.title;
    }
    if (req.body.done !== undefined) {
        task.done = req.body.done;
    }

    res.json(task);
});

app.delete('/tasks/:id', (req, res) => {
    const taskId = parseInt(req.params.id);
    const taskIndex = tasks.findIndex(t => t.id === taskId);

    if (taskIndex === -1) {
        // 404 : not found (server cannot find the requested resource)
        // in browser => the URL is not recognized
        // in API => the endpoint is valid but the resource does not exist
        return res.status(404).json({ error: 'Task not found' });
    }

    // (startingPosition, numberOfRemovedItems)
    tasks.splice(taskIndex, 1);
    // 204 : no content 
    res.status(204).send();
});


app.listen(3000, () => {
    console.log('Server running on port 3000')
});