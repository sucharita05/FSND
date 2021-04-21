import React from 'react';


function Actor({ actors }) {
	console.log(actors);

	return (
		<div>
			<div className="page">
				<nav id="colorlib-main-nav" role="navigation">
					<a href="" className="js-colorlib-nav-toggle colorlib-nav-toggle active"><i></i></a>
					<div className="js-fullheight colorlib-table">
						<div className="img" style={{ backgroundImage: 'url(assets/images/img-2.jfif)' }}></div>
						<div className="colorlib-table-cell js-fullheight">
							<div className="row no-gutters">
								<div className="col-md-12 text-center">
									<h1 className="mb-4"><a href="/" className="logo">Star in Making<br /><span>Casting Agency</span></a></h1>
									<ul>
										<li><a href="/"><span>Home</span></a></li>
										<li><a href="/about"><span>About</span></a></li>
										<li className="active"><a href="/actors"><span>Actors</span></a></li>
										<li><a href="/movies"><span>Movies</span></a></li>
										<li><a href="/contact"><span>Contact</span></a></li>
									</ul>
								</div>
							</div>
						</div>
					</div>
				</nav>

				<div id="colorlib-page">
					<header>
						<div className="container">
							<div className="colorlib-navbar-brand">
								<a href="index.html" className="colorlib-logo">Star In Making<br /><span>Casting Agency</span></a>
							</div>
							<a href="" className="js-colorlib-nav-toggle colorlib-nav-toggle"><i></i></a>
						</div>
					</header>

					<section className="hero-wrap" style={{ backgroundImage: 'url(assets/images/img-7.jpg)' }}>
						<div className="overlay"></div>
						<div className="container">
							<div className="row no-gutters text align-items-end justify-content-center" data-scrollax-parent="true">
								<div className="col-md-8 ftco-animate text-center">
									<p className="breadcrumbs"><span className="mr-2"><a href="index.html">Home</a></span> <span>Actors</span></p>
									<h1 className="mb-5 bread">Our Top Actors</h1>
								</div>
							</div>
						</div>
					</section>

					<section className="ftco-section  ftco-no-pb">
						<div className="container">
							<div className="row justify-content-center">
								<div className="col-md-10 ftco-animate">
									<div className="heading-section text-center mb-5">
										<span className="subheading">Actors</span>
										<h2 className="">Our Tops Actor's</h2>
										<p>are handpicked and boast a varied range of talent.</p>
									</div>
								</div>
							</div>
						</div>
						<div className="container-fluid px-4">
							<div className="row d-flex">
								{actors.map(actor => {
									return (
										<div key={actor.id} className="col-md-6 col-lg-3">
											<div className="model-entry">
												<div className="model-img" style={{ backgroundImage: 'url(' + `${actor.image_link ? actor.image_link : 'assets/images/image_10.jpg'}` + ')' }}>
													<div className="name text-center">
														<h3><a href="">{actor.first_name}</a></h3>
													</div>
													<div className="text text-center">
														<h3><a href="">{actor.first_name}<br /><span>{actor.last_name}</span></a></h3>
														<div className="d-flex models-info">
															<div className="box">
																<p>Age</p>
																<span>{actor.age}</span>
															</div>
															<div className="box">
																<p>Gender</p>
																<span>{actor.gender}</span>
															</div>
															<div className="box">
															<p>Edit</p>
															<p>Delete</p>
															</div>
														</div>
													</div>
												</div>
											</div>
										</div>
									);
								})}
							</div>
						</div>
						{/* <div className="row mt-5">
							<div className="col text-center">
								<div className="block-27">
									<ul>
										<li><a>&lt;</a></li>
										<li className="active"><span>1</span></li>
										<li><a>2</a></li>
										<li><a>3</a></li>
										<li><a>4</a></li>
										<li><a>5</a></li>
										<li><a>&gt;</a></li>
									</ul>
								</div>
							</div>
						</div> */}
					</section>

					<footer className="ftco-footer ftco-section img">
						<div className="overlay"></div>
						<div className="container">
							<div className="row mb-5">
								<div className="col-md-3">
									<div className="ftco-footer-widget mb-4">
										<h2 className="ftco-heading-2 logo"><a href="/">Star In Making</a></h2>
										<p>Becoming a celebrity is now a one step away. Build a portfolio & let it speak for you.</p>
										<ul className="ftco-footer-social list-unstyled float-md-left float-lft mt-5">
											<li className="ftco-animate"><a><span className="icon-twitter"></span></a></li>
											<li className="ftco-animate"><a><span className="icon-facebook"></span></a></li>
											<li className="ftco-animate"><a><span className="icon-instagram"></span></a></li>
										</ul>
									</div>
								</div>
								<div className="col-md-4">
								</div>
								<div className="col-md-2">
									<div className="ftco-footer-widget mb-4 ml-md-4">
										<h2 className="ftco-heading-2">Site Links</h2>
										<ul className="list-unstyled">
											<li><a href="/" className="py-2 d-block">Home</a></li>
											<li><a href="/about" className="py-2 d-block">About</a></li>
											<li><a href="/actors" className="py-2 d-block">Actors</a></li>
											<li><a href="/movies" className="py-2 d-block">Movies</a></li>
											<li><a href="/about" className="py-2 d-block">Services</a></li>
										</ul>
									</div>
								</div>
								<div className="col-md-3">
									<div className="ftco-footer-widget mb-4">
										<h2 className="ftco-heading-2">Reach Us</h2>
										<div className="block-23 mb-3">
											<ul>
												<li><span className="icon icon-map-marker"></span><span className="text">VL Mehta Road, Juhu, Mumbai – 400049, Maharashtra, India</span></li>
												<li><a><span className="icon icon-phone"></span><span className="text">+91 1234 987654</span></a></li>
												<li><a><span className="icon icon-envelope"></span><span className="text">info@starinmaking.com</span></a></li>
											</ul>
										</div>
									</div>
								</div>
							</div>
							<div className="row">
								<div className="col-md-12 text-center">

									<p>Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved</p>
								</div>
							</div>
						</div>
					</footer>

				</div>
			</div>
		</div>
	);
}



export default Actor;