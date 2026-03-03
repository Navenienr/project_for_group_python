import React from 'react'
import S from '../style/Games.module.css' 

const SkeletonLoader = () => {
    const skeletons = Array(12).fill(0)
    return (
        <div className={S.skeleton_wrapper}>
            {skeletons.map((item, index) => (
                <div key={index} className={S.skeleton_card}></div>
            ))}
        </div>
    )
}

export default SkeletonLoader