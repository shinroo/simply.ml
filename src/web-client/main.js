'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var e = React.createElement;

var SimplyMLRequestForm = function (_React$Component) {
	_inherits(SimplyMLRequestForm, _React$Component);

	function SimplyMLRequestForm(props) {
		_classCallCheck(this, SimplyMLRequestForm);

		var _this = _possibleConstructorReturn(this, (SimplyMLRequestForm.__proto__ || Object.getPrototypeOf(SimplyMLRequestForm)).call(this, props));

		_this.state = {
			data: {
				value: "{\n  'data':'test'\n}",
				rows: 3
			},
			options: {
				value: "{\n  'options':'test'\n}",
				rows: 3
			}
		};

		_this.handleDataChange = _this.handleDataChange.bind(_this);
		_this.handleOptionsChange = _this.handleOptionsChange.bind(_this);
		_this.handleSubmit = _this.handleSubmit.bind(_this);
		return _this;
	}

	_createClass(SimplyMLRequestForm, [{
		key: "handleDataChange",
		value: function handleDataChange(event) {
			this.setState({
				data: {
					value: event.target.value,
					rows: event.target.value.split(/\r\n|\r|\n/).length
				}
			});
		}
	}, {
		key: "handleOptionsChange",
		value: function handleOptionsChange(event) {
			this.setState({
				options: {
					value: event.target.value,
					rows: event.target.value.split(/\r\n|\r|\n/).length
				}
			});
		}
	}, {
		key: "handleSubmit",
		value: function handleSubmit(event) {
			alert('Data was submitted: ' + this.state.data.value);
			alert('With these options: ' + this.state.options.value);
			event.preventDefault();
		}
	}, {
		key: "render",
		value: function render() {
			return React.createElement(
				"form",
				{ onSubmit: this.handleSubmit },
				React.createElement(
					"div",
					{ "class": "flex-container" },
					React.createElement(
						"div",
						null,
						React.createElement("textarea", {
							value: this.state.data.value,
							onChange: this.handleDataChange,
							rows: this.state.data.rows
						})
					),
					React.createElement(
						"div",
						null,
						React.createElement("textarea", {
							value: this.state.options.value,
							onChange: this.handleOptionsChange,
							rows: this.state.options.rows
						})
					),
					React.createElement(
						"div",
						null,
						React.createElement("input", { type: "submit", value: "Submit" })
					)
				)
			);
		}
	}]);

	return SimplyMLRequestForm;
}(React.Component);

var domContainer = document.querySelector('#request_form_container');
ReactDOM.render(e(SimplyMLRequestForm), domContainer);