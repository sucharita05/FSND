import React from 'react';

function Movie({ recent_movies, upcoming_movies }) {

	return (
		<div>
			<div className="page">
				<nav id="colorlib-main-nav" role="navigation">
					<a className="js-colorlib-nav-toggle colorlib-nav-toggle active"><i></i></a>
					<div className="js-fullheight colorlib-table">
						<div className="img" style={{ backgroundImage: 'url(assets/images/img-2.jfif)' }}></div>
						<div className="colorlib-table-cell js-fullheight">
							<div className="row no-gutters">
								<div className="col-md-12 text-center">
									<h1 className="mb-4"><a href="index.html" className="logo">Star In Making<br /><span>Casting Agency</span></a></h1>
									<ul>
										<li><a href="/"><span>Home</span></a></li>
										<li><a href="/about"><span>About</span></a></li>
										<li><a href="/actors"><span>Actors</span></a></li>
										<li className="active"><a href="/movies"><span>Movies</span></a></li>
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
								<a className="colorlib-logo" href="/">Star In Making<br /><span>Casting Agency</span></a>
							</div>
							<a className="js-colorlib-nav-toggle colorlib-nav-toggle"><i></i></a>
						</div>
					</header>

					<section className="hero-wrap" style={{ backgroundImage: 'url(assets/images/mv-6.jpg)' }}>
						<div className="overlay"></div>
						<div className="container">
							<div className="row no-gutters text align-items-end justify-content-center" data-scrollax-parent="true">
								<div className="col-md-8 ftco-animate text-center">
									<p className="breadcrumbs"><span className="mr-2"><a href="/">Home</a></span> <span>Movies</span></p>
								</div>
							</div>
						</div>
					</section>

					<section className="ftco-section">
						<div className="container">
							<div className="row justify-content-center">
								<div className="col-md-8 mb-5 heading-section text-center ftco-animate">
									<span className="subheading">Movies</span>
									<h2 className="mb-4">Recent Movies</h2>
								</div>
							</div>
							<div className="row d-flex">
								<div className="col-md-12 d-flex ftco-animate">
									{recent_movies.map(movie => {
										return (
												<div key={movie.id}>
												<div className="blog-entry bg-dark align-self-stretch">
												<a className="block-20" style={{ backgroundImage: 'url(' + `${movie.image_link}` + ')' }}>
												</a>
												<div className="text p-4 d-block">
													<div className="meta mb-3">
													</div>
													<h3 className="heading mt-3"><a>{movie.title}</a></h3>
													<p>{movie.release_date}</p>
													<p><a href="https://in.bookmyshow.com" className="btn btn-primary">Book Tickets</a></p>
												</div>
											</div>
											</div>
											
										);
									})}
								</div>
								</div>
						</div>
					</section>

					<section className="ftco-section">
						<div className="container">
							<div className="row justify-content-center">
								<div className="col-md-8 mb-5 heading-section text-center ftco-animate">
									<h2 className="mb-4">upcoming Movies</h2>
								</div>
							</div>
							<div className="row d-flex">
								<div className="col-md-12 d-flex ftco-animate">
								{upcoming_movies.map(movie => {
										return (
												<div key={movie.id} className="blog-entry bg-dark align-self-stretch">
													<a className="block-20" style={{ backgroundImage: 'url(' + `${movie.image_link}` + ')' }}>
													</a>
													<div className="text p-4 d-block">
														<div className="meta mb-3">
														</div>
														<h3 className="heading mt-3"><a>{movie.title}</a></h3>
														<p>{movie.release_date}</p>
														<p><a href="https://in.bookmyshow.com" className="btn btn-primary">Book Tickets</a></p>
													</div>
											</div>
									);
								})}
								</div>
							</div>
						</div>
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
											<li className="ftco-animate"><a href="#"><span className="icon-twitter"></span></a></li>
											<li className="ftco-animate"><a href="#"><span className="icon-facebook"></span></a></li>
											<li className="ftco-animate"><a href="#"><span className="icon-instagram"></span></a></li>
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
												<li><a href="#"><span className="icon icon-phone"></span><span className="text">+91 1234 987654</span></a></li>
												<li><a href="#"><span className="icon icon-envelope"></span><span className="text">info@starinmaking.com</span></a></li>
											</ul>
										</div>
									</div>
								</div>
							</div>
							<div className="row">
								<div className="col-md-12 text-center">

									<p>Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved.</p>
								</div>
							</div>
						</div>
					</footer>

				</div>
			</div>
		</div>
	)

}


export default Movie;