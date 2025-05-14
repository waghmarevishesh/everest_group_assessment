import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";
import ProjectList from "./projects";

function App() {
  const [projects, setProjects] = useState([]);
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/projects").then((response) => {
      setProjects(response.data.projects);
      console.log(response.data);
    });
  }, []);

  return (
    <>
      <ProjectList
        projectsData={projects}
        addProject={setProjects}
      ></ProjectList>
    </>
  );
}

export default App;
