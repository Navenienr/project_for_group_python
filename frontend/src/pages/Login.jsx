import React, { useState } from "react"
import S from "../style/Login.module.css"
import { NavLink, useNavigate } from "react-router-dom"

const Login = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    username: "",
    password: "",
  })

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/api/core/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: formData.username,
          email: formData.email,
          password: formData.password,
          password2: formData.confirmPassword,
        }),
      })

      const data = await response.json();

      if (data.success) {
        localStorage.setItem("userToken", data.token);
        localStorage.setItem("userName", data.user.username);
        window.dispatchEvent(new Event("authChange"));
        navigate("/");
      } else {
        alert(data.errors || "Ошибка авторизации");
      }
    } catch (error) {
      console.error("Ошибка при логине:", error);
      alert("Не удалось связаться с сервером");
    }
  };

  return (
    <div className={S.container}>
      <header className={S.header}>
        <div className={S.nav_container}>
          <NavLink to="/" className={S.logo}>
            <span className={S.logo_icon}>🎮</span>
            GameForum
          </NavLink>
        </div>
      </header>

      <form onSubmit={handleSubmit} className={S.registration_form}>
        <div className={S.form_group}>
          <label>Имя пользователя:</label>
          <br />
          <input
            className={S.input_field}
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            style={{ width: "100%", padding: "8px" }}
          />
        </div>

        <div className={S.form_group}>
          <label>Пароль:</label>
          <input
            className={S.input_field}
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            style={{ width: "100%", padding: "8px" }}
          />
        </div>

        <button type="submit" className={S.submit_button}>
          Войти
        </button>

        <div className={S.submit_button}>
          <NavLink to="/register" className={S.navlink} >Зарегистрироваться</NavLink>
        </div>
      </form>
    </div>
  );
};

export default Login;
