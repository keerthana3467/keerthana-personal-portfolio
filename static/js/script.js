(function(){
 const loader=document.querySelector('.page-loader');window.addEventListener('load',()=>{if(loader)loader.classList.add('hide')});
 const roles = [
    'Computer Science Student',
    'Python Programmer',
    'Web Developer'
];const roleEl=document.getElementById('typed-role');let roleIndex=0,charIndex=0,deleting=false;
 function typeLoop(){if(!roleEl||window.matchMedia('(prefers-reduced-motion: reduce)').matches){if(roleEl)roleEl.textContent=roles[0];return;}const word=roles[roleIndex];roleEl.textContent=word.substring(0,charIndex);if(!deleting){charIndex++;if(charIndex>word.length){deleting=true;setTimeout(typeLoop,1300);return}}else{charIndex--;if(charIndex<0){deleting=false;roleIndex=(roleIndex+1)%roles.length;charIndex=0}}setTimeout(typeLoop,deleting?40:75)}
 setTimeout(typeLoop,550);
 const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.12});document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
 const nav=document.querySelectorAll('#navmenu .nav-link');nav.forEach(link=>link.addEventListener('click',()=>{const menu=document.querySelector('#navmenu');if(menu&&menu.classList.contains('show')&&window.bootstrap){window.bootstrap.Collapse.getOrCreateInstance(menu).hide()}}));
})();
