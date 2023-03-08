import './App.css';
import React from 'react';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import CreateEvent from "./pages/CreateEvent";
import EventTimeline from "./pages/EventTimeline";
import NotFound from "./pages/NotFound";
import EventInfo from "./pages/EventInfo";
import { Toaster } from "react-hot-toast";


function App() {

    return (
        <div className="app">
            <BrowserRouter>
                <Routes>
                    <Route path="/create" element={<CreateEvent />} />
                    <Route path="/events" element={<EventTimeline />} />
                    <Route path="/events/:event_uuid" element={<EventInfo />} />
                    <Route path="*" element={<NotFound />} />
                </Routes>
            </BrowserRouter>
            <Toaster />
        </div>
    );
}

export default App;
