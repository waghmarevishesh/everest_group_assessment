import React, { useState } from "react";
import Modal from "react-modal";
import "./Project.css";
import axios from "axios";

function ProjectList({ projectsData, addProject }) {
  const [summary, setSummary] = useState({});
  const [isModalOpen, setModalOpen] = useState(false);
  const [newProject, setNewProject] = useState({
    name: "",
    description: "",
    technologies: "",
    image_url: "",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewProject((prev) => ({ ...prev, [name]: value }));
  };

  const handleAddProject = () => {
    if (!newProject.name) {
      alert("Name field is required.");
      return;
    }
    const added = {
      id: projectsData.length + 1,
      name: newProject.name,
      description: newProject.description,
      technologies: newProject.technologies.split(","),
      image_url: newProject.image_url,
    };
    axios
      .post("http://127.0.0.1:8000/api/addproject", added)
      .then((response) => {
        console.log(response);
        addProject((prev) => [...prev, added]);
        alert("Porject added successfuly");
        setModalOpen(false);
        setNewProject({
          name: "",
          description: "",
          technologies: "",
          image_url: "",
        });
      });
  };

  const handleCancel = () => {
    setNewProject({
      name: "",
      description: "",
      technologies: "",
      image_url: "",
    });
    setModalOpen(false);
  };

  const handleSummary = (id) => {
    axios.get(`http://127.0.0.1:8000/api/${id}/getproject`).then((response) => {
      console.log(response);
      setSummary((prev) => {
        if (prev[id]) return { ...prev, [id]: null };
        else return { ...prev, [id]: response.data.response.summary };
      });
    });
  };

  return (
    <div className="prjects-page">
      <div className="header">
        <h1>Projects</h1>
        <button className="add-button" onClick={() => setModalOpen(true)}>
          + Add Project
        </button>
      </div>
      <div className="project-list">
        {projectsData.map((project, index) => (
          <div className="project-card" key={index}>
            <img
              src={project.image_url}
              alt={project.name}
              className="project-image"
            />
            <div className="project-info">
              <h3>{project.name}</h3>
              <p>
                <strong>Technologies:</strong> {project.technologies}
              </p>
              <p>
                <strong>Created:</strong> {project.created_at}
              </p>
              <button onClick={() => handleSummary(project.id)}>
                Generate Summary
              </button>
              {summary[project.id] && (
                <p className="summary">
                  <strong>Summary:</strong> {summary[project.id]}
                </p>
              )}
            </div>
          </div>
        ))}
      </div>
      <Modal
        isOpen={isModalOpen}
        onRequestClose={() => setModalOpen(false)}
        contentLabel="Add Project Modal"
        className="modal"
        overlayClassName="modal-overlay"
      >
        <h3>Add New Project</h3>
        <input
          name="name"
          placeholder="Project Name"
          value={newProject.name}
          onChange={handleInputChange}
        />
        <input
          name="description"
          placeholder="Description"
          value={newProject.description}
          onChange={handleInputChange}
        />
        <input
          name="technologies"
          placeholder="Technologies"
          value={newProject.technologies}
          onChange={handleInputChange}
        />
        <input
          name="image_url"
          placeholder="Image URL"
          value={newProject.image_url}
          onChange={handleInputChange}
        />
        <div className="modal-buttons">
          <button onClick={handleAddProject}>Add</button>
          <button className="cancel" onClick={handleCancel}>
            Cancel
          </button>
        </div>
      </Modal>
    </div>
  );
}

export default ProjectList;
