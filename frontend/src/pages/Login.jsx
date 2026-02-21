import React, { useState, useRef, useEffect } from 'react';
import S from '..//style/Login.module.css';
import Header from "../components/Header";
import {Link, NavLink} from 'react-router-dom'

const Login = () => {
    const [formData, setFormData] = useState({
        email: '',
        username: '',
        phone: ''
    })

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
        ...prevState,
        [name]: value
        }))
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Почта: ${formData.email}\nИмя: ${formData.username}\nТелефон: ${formData.phone}`);
    }



  return (
    
    <div className={S.container}>
        <header className={S.header}>
            <div className={S.nav_container}>
                <NavLink to="/ " className={S.logo}>
                    <span className={S.logo_icon}>🎮</span>
                    GameForum
                </NavLink>
            </div>
        </header>
        <form onSubmit={handleSubmit} className={S.registration_form}>
            <div className={S.form_group}>
                <label>Почта:</label><br />
                <input className={S.input_field} type="email" name="email" 
                    value={formData.email} onChange={handleChange} 
                    required style={{ width: '100%', padding: '8px' }}
                />
            </div>
    
            <div className={S.form_group}>
                <label>Пароль:</label>
                <input className={S.input_field}
                    type="password" name="password" 
                    value={formData.password} onChange={handleChange} 
                    required
                />
            </div>
      
            <button type="submit" className={S.submit_button}>Войти</button>
            <div className={S.submit_button}>
                <NavLink to="/register" className={S.navlink} >Зарегистрироваться</NavLink>
            </div>
            

        </form>
    </div>
  )
}

export default Login